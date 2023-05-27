# Join 연습

````
CREATE TABLE mysql_test_a ( 
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
keyword VARCHAR(30) NOT NULL, 
reaction VARCHAR(50),
number INT
); 


INSERT INTO `mysql_test_a` (`id`, `keyword`, `reaction`, `number`) VALUES ('1', 'test', 'positive', 50);

INSERT INTO `mysql_test_a` (`id`, `keyword`, `reaction`, `number`) VALUES ('3', 'test2', 'positive', 50); 

CREATE TABLE mysql_test_b ( 
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
keyword VARCHAR(30) NOT NULL, 
reaction VARCHAR(50),
number INT
); 



INSERT INTO `mysql_test_b` (`id`, `keyword`, `reaction`, `number`) VALUES ('2', 'test', 'negative', 80); 

INSERT INTO `mysql_test_b` (`id`, `keyword`, `reaction`, `number`) VALUES ('4', 'test2', 'negative', 30); 
```





```
SELECT aa.keyword, 
    IF (aa.number >= bb.number, aa.reaction, bb.reaction) AS reaction,
    IF (aa.number >= bb.number, aa.number, bb.number) AS number

FROM aa

JOIN bb 

ON aa.keyword = bb.keyword

```





CREATE TABLE aa ( 
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
keyword VARCHAR(30) NOT NULL, 
reaction VARCHAR(50),
number INT
); 


INSERT INTO `aa` (`id`, `keyword`, `reaction`, `number`) VALUES ('1', 'keyword1', 'positive', 50);

INSERT INTO `aa` (`id`, `keyword`, `reaction`, `number`) VALUES ('3', 'keyword2', 'positive', 50); 


CREATE TABLE bb ( 
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
keyword VARCHAR(30) NOT NULL, 
reaction VARCHAR(50),
number INT
); 



INSERT INTO `aa` (`id`, `keyword`, `reaction`, `number`) VALUES ('2', 'keyword1', 'negative', 80); 

INSERT INTO `aa` (`id`, `keyword`, `reaction`, `number`) VALUES ('4', 'keyword2', 'negative', 30);

SELECT *
FROM aa
group by aa.id, aa.keyword
````

