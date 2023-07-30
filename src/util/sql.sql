-- SQLite
create table movies (
id integer primary key autoincrement,
name text,
sinopse text,
image text,
video text,
likes integer
);

-- SQLite
delete from movies;

insert into movies (name, sinopse, image, video, likes) values 
('OPPENHEIMER', 'O físico J. Robert Oppenheimer trabalha com uma equipe de cientistas durante o Projeto Manhattan, levando ao desenvolvimento da bomba atômica.', 'https://i.ytimg.com/vi/uYPbbksJxIg/maxresdefault.jpg', 'https://youtu.be/F3OxA9Cz17A', 11);
insert into movies (name, sinopse, image, video, likes) values 
('Tetris', 'Henk Rogers descobre o Tetris em 1988 e arrisca tudo ao viajar para a União Soviética, onde une forças com o inventor Alexey Pajitnov para levar o jogo às massas.', 'https://lvwzvdnyylmpgaeqyqkf.supabase.co/storage/v1/object/sign/students_bk/student.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJzdHVkZW50c19iay9zdHVkZW50LnBuZyIsImlhdCI6MTY5MDYzNzI5MiwiZXhwIjoxNzIyMTczMjkyfQ.hwwtLuewOlZ_bal204VYoQSYXp_O_1wzZrtmYF3-xes&t=2023-07-29T13%3A28%3A12.880Z', 'https://youtu.be/5OtyfVMiXN0', 10);
insert into movies (name, sinopse, image, video, likes) values 
('Barbie', 'Depois de ser expulsa da Barbieland por ser uma boneca de aparência menos do que perfeita, Barbie parte para o mundo humano em busca da verdadeira felicidade.', 'https://lvwzvdnyylmpgaeqyqkf.supabase.co/storage/v1/object/sign/students_bk/student.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJzdHVkZW50c19iay9zdHVkZW50LnBuZyIsImlhdCI6MTY5MDYzNzI5MiwiZXhwIjoxNzIyMTczMjkyfQ.hwwtLuewOlZ_bal204VYoQSYXp_O_1wzZrtmYF3-xes&t=2023-07-29T13%3A28%3A12.880Z', 'https://youtu.be/Ujs1Ud7k49M', 14);
