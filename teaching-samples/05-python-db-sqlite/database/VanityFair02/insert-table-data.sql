PRAGMA foreign_keys = ON;

-- The rows of genre and state must exist before the films that refer to them.

INSERT INTO genre (genre_id, name, short_name)
VALUES (1, 'crime comedy', 'CRCOM'),
       (2, 'gangster', 'GANG'),
       (3, 'romantic comedy', 'ROMCOM'),
       (4, 'crime', 'CRIME'),
       (5, 'comedy', 'COM'),
       (6, 'fantasy', 'FANT'),
       (7, 'science fiction', 'SCIFI');      -- no film of this genre yet

INSERT INTO state (state_id, name, code)
VALUES (1, 'United States of America', 'USA'),
       (2, 'France', 'FRA'),
       (3, 'Yugoslavia', 'YUG'),
       (4, 'Italy', 'ITA');                  -- no film from this state yet

INSERT INTO movie (title, genre_id, state_id, lasting, imdb_score, year, actors, directors, scenarists, plot)
VALUES ('Raising Arizona', 1, 1, 94, 7.3, 1987,
        'Nicolas Cage, Holly Hunter, William Forsythe, John Goodman',
        'Joel Coen', 'Ethan Coen, Joel Coen',
        'A former convict and a police officer, who cannot have children, steal one of the quintuplets of a furniture dealer.');

INSERT INTO movie (title, genre_id, state_id, lasting, imdb_score, year, actors, directors, scenarists, plot)
VALUES ('Miller''s Crossing', 2, 1, 115, 7.7, 1990,
        'Gabriel Byrne, Marcia Gay Harden, John Turturro, Steve Buscemi, Jon Polito',
        'Joel Coen', 'Ethan Coen, Joel Coen',
        'During Prohibition, the adviser of a mob boss plays two rival gangs against each other.');

INSERT INTO movie (title, genre_id, state_id, lasting, imdb_score, year, actors, directors, scenarists, plot)
VALUES ('Amélie', 3, 2, 122, 8.3, 2001,
        'Audrey Tautou, Mathieu Kassovitz',
        'Jean-Pierre Jeunet', 'Guillaume Laurant, Jean-Pierre Jeunet',
        'A shy waitress in Paris decides to secretly improve the lives of the people around her.');

INSERT INTO movie (title, genre_id, state_id, lasting, imdb_score, year, actors, directors, scenarists, plot)
VALUES ('Fargo', 4, 1, 98, 8.1, 1996,
        'Frances McDormand, William H. Macy, Steve Buscemi, Peter Stormare',
        'Joel Coen', 'Ethan Coen, Joel Coen',
        'A car salesman hires two criminals to kidnap his own wife, and a pregnant police chief investigates the murders that follow.');

INSERT INTO movie (title, genre_id, state_id, lasting, imdb_score, year, actors, directors, scenarists, plot)
VALUES ('The Big Lebowski', 1, 1, 117, 8.1, 1998,
        'Jeff Bridges, John Goodman, Julianne Moore, Steve Buscemi',
        'Joel Coen', 'Ethan Coen, Joel Coen',
        'A man who only wants to go bowling is mistaken for a millionaire with the same name.');

INSERT INTO movie (title, genre_id, state_id, lasting, imdb_score, year, actors, directors, scenarists, plot)
VALUES ('O Brother, Where Art Thou?', 5, 1, 107, 7.7, 2000,
        'George Clooney, John Turturro, Tim Blake Nelson, John Goodman',
        'Joel Coen', 'Ethan Coen, Joel Coen',
        'Three escaped convicts search for a hidden treasure in Mississippi of the 1930s.');

INSERT INTO movie (title, genre_id, state_id, lasting, imdb_score, year, actors, directors, scenarists, plot)
VALUES ('No Country for Old Men', 4, 1, 122, 8.2, 2007,
        'Tommy Lee Jones, Javier Bardem, Josh Brolin',
        'Ethan Coen, Joel Coen', 'Ethan Coen, Joel Coen',
        'A hunter finds two million dollars in the desert, and a killer is sent to get the money back.');

INSERT INTO movie (title, genre_id, state_id, lasting, imdb_score, year, actors, directors, scenarists, plot)
VALUES ('Delicatessen', 5, 2, 99, 7.5, 1991,
        'Dominique Pinon, Marie-Laure Dougnac, Jean-Claude Dreyfus',
        'Marc Caro, Jean-Pierre Jeunet', 'Gilles Adrien, Marc Caro, Jean-Pierre Jeunet',
        'In a ruined apartment building, the butcher who is also the landlord has a strange way of feeding his tenants.');

INSERT INTO movie (title, genre_id, state_id, lasting, imdb_score, year, actors, directors, scenarists, plot)
VALUES ('The City of Lost Children', 6, 2, 112, 7.5, 1995,
        'Ron Perlman, Daniel Emilfork, Judith Vittet, Dominique Pinon',
        'Marc Caro, Jean-Pierre Jeunet', 'Gilles Adrien, Jean-Pierre Jeunet',
        'A scientist who cannot dream kidnaps children in order to steal their dreams.');

INSERT INTO movie (title, genre_id, state_id, lasting, imdb_score, year, actors, directors, scenarists, plot)
VALUES ('Who''s Singin'' Over There?', 5, 3, 86, 8.7, 1980,
        'Pavle Vuisić, Dragan Nikolić, Danilo Stojković, Aleksandar Berček, Neda Arnerić',
        'Slobodan Šijan', 'Dušan Kovačević',
        'In April 1941, a group of passengers travels to Belgrade in an old bus.');
