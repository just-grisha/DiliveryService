class Polynomial:
    def __init__(self, *coefficients):
        if len(coefficients) == 1:
            if isinstance(coefficients[0], (list,tuple)):
                self.coefficients = coefficients[0]
            elif isinstance(coefficients[0], dict):
                max_degree = max(coefficients[0].keys())
                self.coefficients = [0] * (max_degree + 1)
                for degree, coef in coefficients[0].items():
                    self.coefficients[degree] = coef
            elif isinstance(coefficients[0], Polynomial):
                self.coefficients = coefficients[0].coefficients[:]
            elif isinstance(coefficients[0], int):
                a = []
                a.append(coefficients[0])
                self.coefficients = a
        else:
            self.coefficients = list(coefficients)

        while self.coefficients and self.coefficients[-1] == 0:
            self.coefficients.pop()

    def __repr__(self):
        return f"Polynomial {self.coefficients}"

    def __str__(self):
        if not self.coefficients:
            return "0"

        def format_term(coef, power):
            if coef == 0:
                return ""
            if power == 0:
                return str(coef)
            term = ""
            if coef != 1 and coef != -1:
                term += str(coef)
            if power == 1:
                term += "x"
            else:
                term += f"x^{power}"
            return term

        terms = []
        for power, coef in enumerate(self.coefficients):
            term = format_term(coef, power)
            if term:
                terms.append(term)

        result = terms[-1]  # первый член (высшая степень) без знака
        for term in terms[-2::-1]:
            result += f" - {term[1:]}" if term[0] == '-' else f" + {term}"

        return result

    def __eq__(self, other):
        # Проверка равенства полиномов
        if isinstance(other, Polynomial):
            return self.coefficients == other.coefficients
        elif isinstance(other, (int, float)):
            return len(self.coefficients) == 1 and self.coefficients[0] == other
        return False

    def __add__(self, other):
        #сложение
        if isinstance(other, Polynomial):
            new_degree = max(self.degree(), other.degree())
            new_coefficients = [0] * (new_degree + 1)
            for i in range(new_degree + 1):
                coef1 = self.coefficients[i] if i < len(self.coefficients) else 0
                coef2 = other.coefficients[i] if i < len(other.coefficients) else 0
                new_coefficients[i] = coef1 + coef2
            return Polynomial(*new_coefficients)
        elif isinstance(other, (int, float)):
            new_coefficients = self.coefficients[:]
            new_coefficients[0] += other
            return Polynomial(new_coefficients)

    def __radd__(self, other):
        # Обратное сложение
        return self.__add__(other)

    def __neg__(self):
        # Отрицание полинома
        return Polynomial(*[-coef for coef in self.coefficients])

    def __sub__(self, other):
        # Вычитание полиномов или числа из полинома
        return self + (-other)

    def __rsub__(self, other):
        # Обратное вычитание
        return -self + other

    def __call__(self, x):
        # Вычисление значения полинома в точке x
        result = 0
        for power, coef in enumerate(self.coefficients):
            result += coef * (x ** power)
        return result

    def degree(self):
        # Определение степени полинома
        return len(self.coefficients) - 1

    def der(self, d=1):
        # Вычисление производной полинома
        new_coefficients = self.coefficients[:]
        for _ in range(d):
            new_coefficients = [i * new_coefficients[i] for i in range(1, len(new_coefficients))]
        return Polynomial(*new_coefficients)

    def __mul__(self, other):
        # Умножение полиномов или полинома на число
        if isinstance(other, Polynomial):
            new_degree = self.degree() + other.degree()
            new_coefficients = [0] * (new_degree + 1)
            for i, coef1 in enumerate(self.coefficients):
                for j, coef2 in enumerate(other.coefficients):
                    new_coefficients[i + j] += coef1 * coef2
            return Polynomial(*new_coefficients)
        elif isinstance(other, (int, float)):
            return Polynomial(*[coef * other for coef in self.coefficients])

    def __rmul__(self, other):
        # Обратное умножение
        return self.__mul__(other)

    def __iter__(self):
        # Итератор по коэффициентам полинома
        self._iter_index = 0
        return self

    def __next__(self):
        # Получение следующего коэффициента
        if self._iter_index >= len(self.coefficients):
            raise StopIteration
        result = (self._iter_index, self.coefficients[self._iter_index])
        self._iter_index += 1
        return result


p1 = Polynomial([1, 2, 3])
p2 = Polynomial([1, 2, 3])
p3 = p1 - p2
p4 = Polynomial(0)
print(p3,p4)