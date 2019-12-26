# where子句(删改查)

## 比较运算符

```
SELECT * FROM class WHERE age % 2 = 1;
SELECT * FROM class WHERE age % 2 != 1;
SELECT * FROM class WHERE age > 8;
SELECT * FROM class WHERE age < 8;
SELECT * FROM class WHERE age >= 8;
SELECT * FROM class WHERE age <= 8;

SELECT * FROM class WHERE score BETWEEN 80 AND 100;
SELECT * FROM class WHERE score NOT BETWEEN 80 AND 100;
SELECT * FROM class WHERE age IN (20,30);
SELECT * FROM class WHERE age NOT IN (20,30);
SELECT * FROM class WHERE sex IS NULL;
SELECT * FROM class WHERE sex IS NOT NULL;
```

## 逻辑运算符

```
SELECT * FROM class WHERE sex='m' AND age>9;
SELECT * FROM class WHERE sex='m' OR age>9;
SELECT * FROM class WHERE NOT age>9;
SELECT * FROM class WHERE age=9 XOR sex="w";
```

## 位运算符

```
SELECT * FROM class WHERE age<<3;
SELECT * FROM class WHERE age>>5;
```

