CREATE TABLE todo_items (
    item_id INT NOT NULL AUTO_INCREMENT, 
    task_description VARCHAR(255), 
    datetime_added DATETIME, 
    datetime_completed DATETIME, 
    done BOOL,
    PRIMARY KEY(item_id));