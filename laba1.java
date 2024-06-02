// Основной класс-родитель
class Transport {
    private String make;
    private String model;
    private int year;
    private double fuelLevel;
    private boolean isRunning;

    public Transport(String make, String model, int year, double fuelLevel) {
        this.make = make;
        this.model = model;
        this.year = year;
        this.fuelLevel = fuelLevel;
        this.isRunning = false;
    }

    public void start() {
        if (!isRunning) {
            isRunning = true;
            System.out.println("Транспортное средство заведено.");
        } else {
            System.out.println("Транспортное средство уже заведено.");
        }
    }

    public void stop() {
        if (isRunning) {
            isRunning = false;
            System.out.println("Транспортное средство остановлено.");
        } else {
            System.out.println("Транспортное средство уже остановлено.");
        }
    }

    public void refuel(double amount) {
        fuelLevel += amount;
        System.out.println("Транспортное средство заправлено. Уровень топлива: " + fuelLevel + " литров.");
    }

    public void displayInfo() {
        System.out.println("Марка: " + make);
        System.out.println("Модель: " + model);
        System.out.println("Год: " + year);
        System.out.println("Уровень топлива: " + fuelLevel + " литров");
        System.out.println("Работает: " + isRunning);
    }

    // Геттеры и сеттеры
    public String getMake() { return make; }
    public void setMake(String make) { this.make = make; }
    public String getModel() { return model; }
    public void setModel(String model) { this.model = model; }
    public int getYear() { return year; }
    public void setYear(int year) { this.year = year; }
    public double getFuelLevel() { return fuelLevel; }
    public void setFuelLevel(double fuelLevel) { this.fuelLevel = fuelLevel; }
    public boolean isRunning() { return isRunning; }
    public void setRunning(boolean running) { isRunning = running; }
}

// Первый наследник
class Bus extends Transport {
    private int numberOfSeats;
    private String transmissionType;

    public Bus(String make, String model, int year, double fuelLevel, int numberOfSeats, String transmissionType) {
        super(make, model, year, fuelLevel);
        this.numberOfSeats = numberOfSeats;
        this.transmissionType = transmissionType;
    }

    public void changeTransmission(String newTransmissionType) {
        this.transmissionType = newTransmissionType;
        System.out.println("Тип трансмиссии изменен на: " + this.transmissionType);
    }

    public void lockDoors() {
        System.out.println("Все двери заблокированы.");
    }

    @Override
    public void displayInfo() {
        super.displayInfo();
        System.out.println("Количество мест: " + numberOfSeats);
        System.out.println("Тип трансмиссии: " + transmissionType);
    }

    // Геттеры и сеттеры
    public int getNumberOfSeats() { return numberOfSeats; }
    public void setNumberOfSeats(int numberOfSeats) { this.numberOfSeats = numberOfSeats; }
    public String getTransmissionType() { return transmissionType; }
    public void setTransmissionType(String transmissionType) { this.transmissionType = transmissionType; }
}

// Второй наследник
class ElectricBus extends Bus {
    private double batteryLevel;
    private int range;

    public ElectricBus(String make, String model, int year, double fuelLevel, int numberOfSeats, String transmissionType, double batteryLevel, int range) {
        super(make, model, year, fuelLevel, numberOfSeats, transmissionType);
        this.batteryLevel = batteryLevel;
        this.range = range;
    }

    public void chargeBattery(double amount) {
        this.batteryLevel += amount;
        System.out.println("Аккумулятор заряжен. Текущий уровень заряда: " + this.batteryLevel + " кВт*ч.");
    }

    public void updateRange(int newRange) {
        this.range = newRange;
        System.out.println("Запас хода обновлен до: " + this.range + " км.");
    }

    @Override
    public void displayInfo() {
        super.displayInfo();
        System.out.println("Уровень заряда аккумулятора: " + batteryLevel + " кВт*ч");
        System.out.println("Запас хода: " + range + " км");
    }

    // Геттеры и сеттеры
    public double getBatteryLevel() { return batteryLevel; }
    public void setBatteryLevel(double batteryLevel) { this.batteryLevel = batteryLevel; }
    public int getRange() { return range; }
    public void setRange(int range) { this.range = range; }
}

// Главный класс для тестирования
public class Main {
    public static void main(String[] args) {
        Transport transport = new Transport("lada", "granta", 2020, 100.0);
        Bus bus = new Bus("39", "avtobik", 2019, 120.0, 30, "Автоматическая");
        ElectricBus electricBus = new ElectricBus("50", "avtobik", 2021, 0, 40, "Автоматическая", 200.0, 300);

        System.out.println("Информация о транспортном средстве:");
        transport.displayInfo();
        transport.start();
        transport.refuel(50);

        System.out.println("\nИнформация об автобусе:");
        bus.displayInfo();
        bus.changeTransmission("Механическая");
        bus.lockDoors();

        System.out.println("\nИнформация об электроавтобусе:");
        electricBus.displayInfo();
        electricBus.chargeBattery(50);
        electricBus.updateRange(400);
    }
}
