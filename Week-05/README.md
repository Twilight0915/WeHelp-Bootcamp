# Week-05 Assignment 要求三、四部分

SHOW DATABASES;  </br>
CREATE DATABASE website;  </br>
USE website;  </br>
SHOW TABLES;  </br>
CREATE TABLE member(
	id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    follower_count INT UNSIGNED NOT NULL DEFAULT 0,
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);   
</br>
</br>
INSERT INTO member(id,name,username,password,follower_count) 
VALUES(1,'Ian','test','test',50);   </br>

![image](https://user-images.githubusercontent.com/104882761/197391543-ef5c52e2-32c3-4eda-a378-19d61f84ebc3.png)


INSERT INTO member(id,name,username,password,follower_count) 
VALUES (2,'Tom','apple','red',40);

INSERT INTO member(name,username,password,follower_count) 
VALUES ('John','banana','yellow',30);

INSERT INTO member(name,username,password,follower_count) 
VALUES ('Brian','cat','white',20);

INSERT INTO member(name,username,password,follower_count) 
VALUES ('Ken','dog','black',10);
</br>

SELECT * FROM member;
![image](https://user-images.githubusercontent.com/104882761/197391735-42bd1ee2-5661-426e-8de6-8c4aa9d7ff5a.png)
</br>

SELECT * FROM member ORDER BY time DESC;
SELECT * FROM(
	SELECT *, ROW_NUMBER() OVER (ORDER BY time DESC) AS ROW_ID FROM member
) time_desc_table WHERE ROW_ID >=2 and ROW_ID <=4;

SELECT * FROM member WHERE username='test';
SELECT * FROM member WHERE username='test' and password='test';
UPDATE member SET name='test2' WHERE username='test';
UPDATE member SET name='Ian' WHERE username='test';

SELECT COUNT( * ) FROM member;
SELECT SUM(follower_count) FROM member;
SELECT AVG(follower_count) FROM member;
