-- Users data

-- timothy/Timothy12
INSERT INTO users(username, name, email, password)
VALUES ("timothy", "Tim Spencer", "timspencer@gmail.com", "sha256$GI7UXUkx$196af489b1d42fdab373ffab311654bece4ba37d1eacd1d5eac8d31bfc0a8d11");

-- robert/robertdavis89
INSERT INTO users(username, name, email, password)
VALUES ("robert", "Robert David", "robertdavis@gmail.com", "sha256$KpHD3Omm$fe9272ea209d585aaf3c9e17225906bbfc549a161ede045d57da2ebc55b6a3de");

-- taylor/taylortran91
INSERT INTO users(username, name, email, password)
VALUES ("taylor", "Taylor Tran", "taylortran91@gmail.com", "sha256$j6u9KYDu$f8514ce9d60632b7ae10ab2dae84d11e383a677dfa746e6eee0832f59a374607");

-- Categories data

INSERT INTO categories(name, description)
VALUES ("Laptop", "Electronics Laptop");

INSERT INTO categories(name, description)
VALUES ("Television", "Machine being used to watch programs or channel from stations");

INSERT INTO categories(name, description)
VALUES ("Food", "What do you eat?");

INSERT INTO categories(name, description)
VALUES ("Clothes", "What do you wear today?");

INSERT INTO categories(name, description)
VALUES ("Vehicle", "Machine that people use to commute between physical locations");


-- Items data

INSERT INTO items(name, description, price, category_id, user_id)
VALUES("DellXPS", "This is a really good laptop", 1500.0, 1, 1);

INSERT INTO items(name, description, price, category_id, user_id)
VALUES("MacPro", "Possibly the best laptop overall", 1800.0, 1, 2);

INSERT INTO items(name, description, price, category_id, user_id)
VALUES("HPSpectre", "Looks really cool", 1100.0, 1, 3);

INSERT INTO items(name, description, price, category_id, user_id)
VALUES("ChromeBook", "Lightweight laptop for work", 600.0, 1, 2);