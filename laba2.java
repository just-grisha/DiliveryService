import java.util.concurrent.Semaphore;

class Salon {
    private final int NUM_SEATS = 5;
    private final Semaphore clientSemaphore = new Semaphore(0);
    private final Semaphore stylistSemaphore = new Semaphore(0);
    private final Semaphore seatAccessSemaphore = new Semaphore(1);

    private int waitingClients = 0;

    class Stylist extends Thread {
        public void run() {
            while (true) {
                try {
                    System.out.println("Парикмахер засыпает из-за отсутствия клиентов.");
                    clientSemaphore.acquire();
                    System.out.println("Парикмахер просыпается, так как появился клиент.");

                    seatAccessSemaphore.acquire();
                    if (waitingClients > 0) {
                        waitingClients--;
                        stylistSemaphore.release();
                    }
                    seatAccessSemaphore.release();

                    cutHair();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }

        private void cutHair() {
            System.out.println("Парикмахер проводит стрижку клиента.");
            try {
                Thread.sleep(4000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    class Client extends Thread {
        public void run() {
            try {
                seatAccessSemaphore.acquire();
                if (waitingClients < NUM_SEATS) {
                    waitingClients++;
                    System.out.println("Клиент занимает место в ожидании. Число ожидающих: " + waitingClients);
                    clientSemaphore.release();
                    seatAccessSemaphore.release();
                    stylistSemaphore.acquire();
                    getHaircut();
                } else {
                    System.out.println("Клиент уходит, так как нет свободных мест.");
                    seatAccessSemaphore.release();
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        private void getHaircut() {
            System.out.println("Клиент получает стрижку.");
        }
    }

    public static void main(String[] args) {
        Salon salon = new Salon();
        Stylist stylist = salon.new Stylist();
        stylist.start();

        for (int i = 0; i < 20; i++) {
            Client client = salon.new Client();
            client.start();
            try {
                Thread.sleep((int)(Math.random() * 3000));
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}