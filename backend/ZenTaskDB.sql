SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS Users;
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT,
    firstname VARCHAR(30) NOT NULL,
    lastname VARCHAR(30) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL,
    PRIMARY KEY(user_id)
);

LOCK TABLES `Users` WRITE;
INSERT INTO Users (firstname, lastname, username, email, password) VALUES
('Alice', 'Johnson', 'alicej', 'alice.johnson@example.com', 'hashed_password_1'),
('Bob', 'Smith', 'bobsmith', 'bob.smith@example.com', 'hashed_password_2'),
('Charlie', 'Brown', 'charlieb', 'charlie.brown@example.com', 'hashed_password_3'),
('Diana', 'Prince', 'dianap', 'diana.prince@example.com', 'hashed_password_4'),
('Eve', 'Adams', 'evea', 'eve.adams@example.com', 'hashed_password_5');
UNLOCK TABLES;

DROP TABLE IF EXISTS Goals;
CREATE TABLE Goals (
    goal_id INT AUTO_INCREMENT,
    goal_type_id ENUM("Personal", "Professional", "Health"),
    goal_status ENUM('pending', 'done') NOT NULL,
    task_id INT,
    PRIMARY KEY(goal_id)
);

DROP TABLE IF EXISTS Sessions;
CREATE TABLE Sessions (
    session_id INT AUTO_INCREMENT,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    duration TIME NOT NULL,
    breaks INT NOT NULL,
    mood_id INT,
    task_id INT,
    PRIMARY KEY(session_id)
);

DROP TABLE IF EXISTS Tasks;
CREATE TABLE Tasks (
    task_id INT AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(180) NOT NULL,
    priority ENUM("urgent, important", "not urgent, important", "urgent, not important", "not urgent, not important") NOT NULL,
    user_id INT,
    session_id INT,
    goal_id INT,
    PRIMARY KEY(task_id)
);

DROP TABLE IF EXISTS Moods;
CREATE TABLE Moods (
    mood_id INT AUTO_INCREMENT,
    mood_status ENUM('Happy', 'Sad', 'Cry', 'Exclaimed', 'Strong') NOT NULL,
    session_id INT,
    PRIMARY KEY(mood_id)
);

ALTER TABLE Tasks
    ADD FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    ADD FOREIGN KEY (session_id) REFERENCES Sessions(session_id) ON DELETE CASCADE,
    ADD FOREIGN KEY (goal_id) REFERENCES Goals(goal_id) ON DELETE CASCADE;

LOCK TABLES `Tasks` WRITE;
INSERT INTO Tasks (title, description, priority, user_id, session_id, goal_id) VALUES
('Finish project report', 'Complete the final report for the project.', 'urgent, important', 1, NULL, 1),
('Attend conference', 'Participate in the annual tech conference.', 'not urgent, important', 2, NULL, 2),
('Morning run', 'Run 5km in the morning.', 'urgent, not important', 3, NULL, 3),
('Grocery shopping', 'Buy groceries for the week.', 'not urgent, not important', 4, NULL, 4),
('Yoga session', 'Attend a yoga class.', 'urgent, important', 5, NULL, 5);
UNLOCK TABLES;

ALTER TABLE Sessions
    ADD FOREIGN KEY (mood_id) REFERENCES Moods(mood_id) ON DELETE SET NULL,
    ADD FOREIGN KEY (task_id) REFERENCES Tasks(task_id) ON DELETE CASCADE;

LOCK TABLES `Sessions` WRITE;
INSERT INTO Sessions (start_time, end_time, duration, breaks, mood_id, task_id) VALUES
('2024-08-26 08:00:00', '2024-08-26 09:00:00', '01:00:00', 1, NULL, 1),
('2024-08-26 10:00:00', '2024-08-26 11:30:00', '01:30:00', 2, NULL, 2),
('2024-08-26 14:00:00', '2024-08-26 15:00:00', '01:00:00', 0, 3, 3),
('2024-08-26 16:00:00', '2024-08-26 16:45:00', '00:45:00', 1, 4, 4),
('2024-08-26 18:00:00', '2024-08-26 19:00:00', '01:00:00', 2, NULL, 5);
UNLOCK TABLES;

ALTER TABLE Goals
    ADD FOREIGN KEY (task_id) REFERENCES Tasks(task_id) ON DELETE CASCADE;

LOCK TABLES `Goals` WRITE;
INSERT INTO Goals (goal_type_id, goal_status, task_id) VALUES
('Personal', 'pending', NULL),
('Professional', 'done', NULL),
('Health', 'pending', NULL),
('Personal', 'done', NULL),
('Health', 'pending', NULL);
UNLOCK TABLES;

ALTER TABLE Moods
    ADD FOREIGN KEY (session_id) REFERENCES Sessions(session_id) ON DELETE CASCADE;

LOCK TABLES `Moods` WRITE;
INSERT INTO Moods (mood_status, session_id) VALUES
('Happy', 1),
('Sad', 2),
('Exclaimed', 3),
('Strong', 4),
('Cry', 5);
UNLOCK TABLES;

SET FOREIGN_KEY_CHECKS = 1;
