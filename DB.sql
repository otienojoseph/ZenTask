ers Table
CREATE TABLE Users (
	    user_id INT PRIMARY KEY AUTO_INCREMENT,
	    first_name VARCHAR(30) NOT NULL,
	    surname VARCHAR(30) NOT NULL,
	    username VARCHAR(50) NOT NULL UNIQUE,
	    email VARCHAR(100) NOT NULL UNIQUE,
	    password VARCHAR(128) NOT NULL
);

-- GoalTypes Table with ENUM values in a Column (theoretical)
-- (Note: This is not typical use for ENUM and wouldn't populate 'rows')
CREATE TABLE UpdatedGoalTypes (
	    goal_type_id INT PRIMARY KEY AUTO_INCREMENT,
	    goal_type ENUM('Personal', 'Professional', 'Health') NOT NULL UNIQUE
);

-- Tasks Table
CREATE TABLE Tasks (
	    task_id INT PRIMARY KEY AUTO_INCREMENT,
	    title VARCHAR(100) NOT NULL,
	    description VARCHAR(180) NOT NULL,
	    priority VARCHAR(50) NOT NULL,
	    user_id INT,
	    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

-- Goals Table
CREATE TABLE Goals (
	    goal_id INT PRIMARY KEY AUTO_INCREMENT,
	    priority ENUM('urgent, important', 'not urgent, important', 'urgent, not important', 'not urgent, not important') NOT NULL,
	    goal_type_id INT,
	    task_id INT,
	    FOREIGN KEY (goal_type_id) REFERENCES UpdatedGoalTypes(goal_type_id) ON DELETE CASCADE,
	    FOREIGN KEY (task_id) REFERENCES Tasks(task_id) ON DELETE CASCADE
);

-- GoalStatus Table
CREATE TABLE GoalStatus (
	    goal_status_id INT PRIMARY KEY AUTO_INCREMENT,
	    goal_status ENUM('pending', 'done') NOT NULL,
	    goal_id INT,
	    FOREIGN KEY (goal_id) REFERENCES Goals(goal_id) ON DELETE CASCADE
);

-- Sessions Table
CREATE TABLE Sessions (
	    session_id INT PRIMARY KEY AUTO_INCREMENT,
	    start_time DATETIME NOT NULL,
	    end_time DATETIME NOT NULL,
	    duration TIME NOT NULL,
	    breaks INT NOT NULL,
	    mood_id INT,
	    task_id INT,
	    FOREIGN KEY (mood_id) REFERENCES Moods(mood_id) ON DELETE SET NULL,
	    FOREIGN KEY (task_id) REFERENCES Tasks(task_id) ON DELETE CASCADE
);

-- Moods Table
CREATE TABLE Moods (
	    mood_id INT PRIMARY KEY AUTO_INCREMENT,
	    mood_status ENUM('Happy', 'Sad', 'Cry', 'Exclaimed', 'Strong') NOT NULL,
	    session_id INT,
	    FOREIGN KEY (session_id) REFERENCES Sessions(session_id)
);
