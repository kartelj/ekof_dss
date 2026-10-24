-- The column movie_id is not mentioned: the DBMS assigns its values.
-- The column profit is not mentioned either, so it gets its default value 0.
-- A quote inside a text is written twice: 'Miller''s Crossing'.

INSERT INTO movie (title, genre, states, lasting, imdb_score, year, actors, directors, scenarists, plot)
VALUES ('Raising Arizona', 'crime comedy', 'USA', 94, 7.3, 1987,
        'Nicolas Cage, Holly Hunter, William Forsythe, John Goodman',
        'Joel Coen', 'Ethan Coen, Joel Coen',
        'A former convict and a police officer, who cannot have children, steal one of the quintuplets of a furniture dealer.');

INSERT INTO movie (title, genre, states, lasting, imdb_score, year, actors, directors, scenarists, plot)
VALUES ('Miller''s Crossing', 'gangster', 'USA', 115, 7.7, 1990,
        'Gabriel Byrne, Marcia Gay Harden, John Turturro, Steve Buscemi, Jon Polito',
        'Joel Coen', 'Ethan Coen, Joel Coen',
        'During Prohibition, the adviser of a mob boss plays two rival gangs against each other.');

INSERT INTO movie (title, genre, states, lasting, imdb_score, year, actors, directors, scenarists, plot)
VALUES ('Amélie', 'romantic comedy', 'France', 122, 8.3, 2001,
        'Audrey Tautou, Mathieu Kassovitz',
        'Jean-Pierre Jeunet', 'Guillaume Laurant, Jean-Pierre Jeunet',
        'A shy waitress in Paris decides to secretly improve the lives of the people around her.');

INSERT INTO movie (title, genre, states, lasting, imdb_score, year, actors, directors, scenarists, plot)
VALUES ('Fargo', 'crime', 'USA', 98, 8.1, 1996,
        'Frances McDormand, William H. Macy, Steve Buscemi, Peter Stormare',
        'Joel Coen', 'Ethan Coen, Joel Coen',
        'A car salesman hires two criminals to kidnap his own wife, and a pregnant police chief investigates the murders that follow.');

INSERT INTO movie (title, genre, states, lasting, imdb_score, year, actors, directors, scenarists, plot)
VALUES ('The Big Lebowski', 'crime comedy', 'USA', 117, 8.1, 1998,
        'Jeff Bridges, John Goodman, Julianne Moore, Steve Buscemi',
        'Joel Coen', 'Ethan Coen, Joel Coen',
        'A man who only wants to go bowling is mistaken for a millionaire with the same name.');

INSERT INTO movie (title, genre, states, lasting, imdb_score, year, actors, directors, scenarists, plot)
VALUES ('O Brother, Where Art Thou?', 'comedy', 'USA', 107, 7.7, 2000,
        'George Clooney, John Turturro, Tim Blake Nelson, John Goodman',
        'Joel Coen', 'Ethan Coen, Joel Coen',
        'Three escaped convicts search for a hidden treasure in Mississippi of the 1930s.');

INSERT INTO movie (title, genre, states, lasting, imdb_score, year, actors, directors, scenarists, plot)
VALUES ('No Country for Old Men', 'crime', 'USA', 122, 8.2, 2007,
        'Tommy Lee Jones, Javier Bardem, Josh Brolin',
        'Ethan Coen, Joel Coen', 'Ethan Coen, Joel Coen',
        'A hunter finds two million dollars in the desert, and a killer is sent to get the money back.');

INSERT INTO movie (title, genre, states, lasting, imdb_score, year, actors, directors, scenarists, plot)
VALUES ('Delicatessen', 'comedy', 'France', 99, 7.5, 1991,
        'Dominique Pinon, Marie-Laure Dougnac, Jean-Claude Dreyfus',
        'Marc Caro, Jean-Pierre Jeunet', 'Gilles Adrien, Marc Caro, Jean-Pierre Jeunet',
        'In a ruined apartment building, the butcher who is also the landlord has a strange way of feeding his tenants.');

INSERT INTO movie (title, genre, states, lasting, imdb_score, year, actors, directors, scenarists, plot)
VALUES ('The City of Lost Children', 'fantasy', 'France', 112, 7.5, 1995,
        'Ron Perlman, Daniel Emilfork, Judith Vittet, Dominique Pinon',
        'Marc Caro, Jean-Pierre Jeunet', 'Gilles Adrien, Jean-Pierre Jeunet',
        'A scientist who cannot dream kidnaps children in order to steal their dreams.');

INSERT INTO movie (title, genre, states, lasting, imdb_score, year, actors, directors, scenarists, plot)
VALUES ('Who''s Singin'' Over There?', 'comedy', 'Yugoslavia', 86, 8.7, 1980,
        'Pavle Vuisić, Dragan Nikolić, Danilo Stojković, Aleksandar Berček, Neda Arnerić',
        'Slobodan Šijan', 'Dušan Kovačević',
        'In April 1941, a group of passengers travels to Belgrade in an old bus.');
