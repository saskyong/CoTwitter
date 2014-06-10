CREATE TABLE tweets(
    tweet_id INT NOT NULL auto_increment,
    user_id INT NOT NULL,
    content VARCHAR(140) NOT NULL,
    url_media VARCHAR,
    PRIMARY KEY(id),
    FOREIGN KEY user_id(user_id) REFERENCES users(user_id)
    ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE users(
    user_id INT NOT NULL auto_increment,
    user_name VARCHAR(255) NOT NULL,
    password VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    PRIMARY KEY (user_id)
);

CREATE TABLE followers(
    id_user INT NOT NULL REFERENCES users (user_id),
    id_following INT NOT NULL REFERENCES users (user_id),
    PRIMARY KEY (id_user, id_following)
);
