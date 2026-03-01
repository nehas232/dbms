CREATE TABLE Student (
    student_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE,
    phone VARCHAR(15) NOT NULL
);



CREATE TABLE Author (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(50) NOT NULL,
    country VARCHAR(30)
);


CREATE TABLE Book (
    book_id INT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    price DECIMAL(8,2),
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES Author(author_id)
);





CREATE TABLE Staff (
    staff_id INT PRIMARY KEY,
    staff_name VARCHAR(50),
    designation VARCHAR(30)
);



CREATE TABLE Issue (
    issue_id INT PRIMARY KEY,
    student_id INT,
    book_id INT,
    staff_id INT,
    issue_date DATE,
    return_date DATE,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id),
    FOREIGN KEY (staff_id) REFERENCES Staff(staff_id)
);

INSERT INTO Student VALUES
(1,'Rahul','rahul@gmail.com','9800000001'),
(2,'Anita','anita@gmail.com','9800000002'),
(3,'Sita','sita@gmail.com','9800000003'),
(4,'Ram','ram@gmail.com','9800000004'),
(5,'Hari','hari@gmail.com','9800000005');

INSERT INTO Author VALUES
(1,'R.K. Narayan','India'),
(2,'Chetan Bhagat','India'),
(3,'J.K. Rowling','UK'),
(4,'Paulo Coelho','Brazil'),
(5,'Dan Brown','USA');



INSERT INTO Book VALUES
(1,'Malgudi Days',350,1),
(2,'Half Girlfriend',400,2),
(3,'Harry Potter',800,3),
(4,'The Alchemist',500,4),
(5,'Da Vinci Code',650,5);


INSERT INTO Staff VALUES
(1,'Mr. Sharma','Librarian'),
(2,'Ms. Kiran','Assistant'),
(3,'Mr. Singh','Clerk'),
(4,'Mrs. Devi','Manager'),
(5,'Mr. Roy','Assistant');



INSERT INTO Issue VALUES
(1,1,3,1,'2026-02-01','2026-02-10'),
(2,2,1,2,'2026-02-02','2026-02-12'),
(3,3,2,1,'2026-02-03','2026-02-11'),
(4,4,5,3,'2026-02-04','2026-02-15'),
(5,5,4,2,'2026-02-05','2026-02-14');



SELECT s.name, b.title
FROM Issue i
INNER JOIN Student s ON i.student_id = s.student_id
INNER JOIN Book b ON i.book_id = b.book_id;


SELECT s.name, b.title
FROM Student s
LEFT JOIN Issue i ON s.student_id = i.student_id
LEFT JOIN Book b ON i.book_id = b.book_id;


SELECT s.name, COUNT(i.issue_id) AS total_books
FROM Student s
JOIN Issue i ON s.student_id = i.student_id
GROUP BY s.name;

SELECT AVG(price) AS average_price
FROM Book;



SELECT name
FROM Student
WHERE student_id IN (
    SELECT student_id
    FROM Issue
    WHERE book_id IN (
        SELECT book_id
        FROM Book
        WHERE price > (SELECT AVG(price) FROM Book)
    )
);



CREATE VIEW Issued_Book_Details AS
SELECT s.name, b.title, i.issue_date
FROM Issue i
JOIN Student s ON i.student_id = s.student_id
JOIN Book b ON i.book_id = b.book_id;

SELECT * FROM Issued_Book_Details;

START TRANSACTION;

INSERT INTO Student VALUES (6,'New Student','new@gmail.com','9800000006');

COMMIT;


START TRANSACTION;

INSERT INTO Student VALUES (7,'Temporary Student','temp@gmail.com','9800000007');

ROLLBACK;

