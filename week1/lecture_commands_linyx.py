ls(list)->возвращает список всех папок и файлов текущей директории
ls test-> показывает все папки и файлы директории(папки)test
ls -a -> также показывает скрытые папки и файлы
ls -l -> показывает более подробную информацию
cd -> переходит в домашнюю директорию
cd ~ -> переходит в домашнюю директорию
cd test ->  переходит в директорию test
cd. ->переходит в текущую директорию ( остаемся в ней же)
cd..->переходит на директорию  выше ( переходит в предыдущую папку)
cd../..-> переходит на две директории выше
cd test/test1-> переходит в папку test1,которая находится в папке test
mkdir test -> создает папку test
mkdir test/test1 -> создает папку test1 в папке test
mkdir test1 test2 -> создает папку test1 и test2

touch test.txt -> создает файл test.txt
touch test/test.txt->создает файл test.txt в папке test
touch text /txt test2.txt->создает файлы test.txt и test2.txt
touch test{3,4}.txt-> создает файлы test3.txt и test.txt

rm test.txt-> удаляет файл test.txt
rmdir -> удаляет пустую директорию
rm-rf test-> удаляет папку test со всем содержимым
rm- rf/ -> удаляет корневую папку НИКОГДА НЕ ПИСАТЬ

cat test.txt -> показывает содержимое файла test.txt
cat test.txt > test.txt -> скопирует содержимое  файла test.tx
в файле test1.txt

nano test.txt -> открывает файл test.txt в текстовом редакторе( в терминале)

mv-> переместить или переименовать файл
mv test.txt commands.txt -> переименует файл test.txt в commands.test
mv test.txt test -> перемещает файл  test.txt  в директорию test

echo text > test.txt ->перезаписывает текст в файл test.txt
echo text >>test.txt -> перезаписывает text в файл test.txt

clear -> очищает терминал

cp test.txt test1.txt -> копирует содержимое файла test.txt в файл test.txt
cp test.txt test -> копирует файл test.txt в директорию test

history -> выводит историю терминала

sudo <command> -> выполняет команду с правами администратора
sudo apt update -> скачивает последние версии ваших предложений
нажатие на клавишу Tab -> приводит к автозаполнению


