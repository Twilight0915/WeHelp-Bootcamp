# Week-05 Assignment 要求三、四部分

SHOW DATABASES;  </br>
CREATE DATABASE website;  </br>
USE website;  </br>
SHOW TABLES;  </br>
CREATE TABLE member(   </br> 
	id BIGINT PRIMARY KEY AUTO_INCREMENT,        
    name VARCHAR(255) NOT NULL,  </br>
    username VARCHAR(255) NOT NULL,  </br>
    password VARCHAR(255) NOT NULL,  </br>
    follower_count INT UNSIGNED NOT NULL DEFAULT 0,  </br>
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP  </br>
);   
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
![image](https://user-images.githubusercontent.com/104882761/197391984-b7dce0a0-a10e-4de7-95af-a1ef054e9e7d.png)
</br>

SELECT * FROM(
	SELECT *, ROW_NUMBER() OVER (ORDER BY time DESC) AS ROW_ID FROM member
) time_desc_table WHERE ROW_ID >=2 and ROW_ID <=4;
</br>
SELECT * FROM member WHERE username='test';
</br>
SELECT * FROM member WHERE username='test' and password='test';
</br>
UPDATE member SET name='test2' WHERE username='test';
</br>
SELECT COUNT( * ) FROM member;
</br>
SELECT SUM(follower_count) FROM member;
</br>
SELECT AVG(follower_count) FROM member;
