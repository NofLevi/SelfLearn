#include <iostream>
#include <cmath>

using namespace std;

class Book {
public:
    string title;
    string auth;
    int pages;

    Book(string aTitle, string aAuth, int aPages)
    {
        title = aTitle;
        auth = aAuth;
        pages = aPages;
    }

    void CheckFunction()
    {
        if(title != "")
        {
            cout << "Oka";
        }
        else
        {
            cout << "Not oka";
        }
    }
};

void sayHi(string name)
{
    cout << name << " Hello World!!!";
}

int cube(int num)
{
    return num*num;
}

string switchExample(int num)
{
    string example;
    switch(num)
    {
    case 0:
        example = "yonatan";
        //return or break to stop the functions
        break;
    case 1:
        example = "akatan";
        break;
    default:
        example = "ratz";
    }
    return example;
}



int main()
{
    //Basic Variables
    /*
    string characterName = "John";
    int charactherAge = 35;

    cout << "There once was a man named " << characterName << endl;
    cout << "He was " << charactherAge << " years old" << endl;
    cout << "He liked the name " << charactherAge << endl;
    cout << "But did not like being " << charactherAge << endl;
    */

    /*
    char grade = 'A';
    string phrase = "Girrafe Aacademy";
    int age = 50;
    float gpaa = 2.3;
    double gpa = 2.3;
    bool isMale = false;

    cout << phrase << endl;
    */


    //String Functions
    /*
    string phrase = "Girrafe Academy";
    cout << phrase[0] << endl;
    phrase[0] = 'B'; //change var
    cout << phrase << endl;
    int len = phrase.length(); //get string length
    cout << phrase.find("Academy", 0) << endl; //which word and from where to search return the position where is begins
    string temp = phrase.substr(8,3);  //from which position to take and how many positions after
    cout << temp << endl;
    */


    //Numbers Functions
    /*
    int wnum = 5;
    double dnum = 5.5;

    cout << wnum + dnum << endl; //int + float or double is equal float or double
    cout << 10 / 3 << endl; //int + int is equal int even if the answer is incurrect
    cout << pow(2, 5) << endl; // pow
    cout << sqrt(36) << endl; //square root
    cout << round(4.3) << endl; //get int to closer number
    cout << ceil(4.1) << endl; //round if to upper
    cout << floor(4.1) << endl; //round up
    cout << fmax(3,10) << endl; // telling which 1 is bigger
    cout << fmin(3,10) << endl1; // teling which 1 is smaller
    */

    //User input

    /*
    int age;
    cout << "Enter your age: ";
    cin >> age; // get int/char
    cout << "You are " << age << " Years Old." << endl << endl;

    cin.clear(); //clear cin
    fflush(stdin); //flush sin

    string name;
    cout << "Enter your name: " << endl;
    getline(cin, name); //get string
    cout << "Hello " << name << "!!!!" << endl;
    */

    //Making Calculator
    /*
    int num1, num2;

    cout << "Enter First number: ";
    cin >> num1;

    cout << "Enter second number: ";
    cin >> num2;

    cout << num1 + num2;
    */

    //Making MadLibs
    /*
    string color, pluralNoun, celebritiy;
    cout << "enter a color: ";
    getline(cin, color);
    cout << "enter a plural noun: ";
    getline(cin, pluralNoun);
    cout << "enter a celebrity: ";
    getline(cin, celebritiy);

    cout << "Roses are " << color << endl;
    cout << pluralNoun << " are blue" << endl;
    cout << "i love " << celebritiy << endl;
    */

    //Array
    /*
    int luckyNums[] = {4, 8, 15, 16, 23,42};

    cout << luckyNums[2];
    */

    //Functions
    /*
    string name;

    cout << "Enter your Full Name: ";
    //cin >> name // wont get the full name space stopping it
    getline(cin, name); // to get full name
    sayHi(name);


    int num;
    cout << "Enter a num: ";
    cin >> num;
    num = cube(num);
    cout << num;
    */

    //2D Array
    /*
    int numberGrid[3][2] = {
                                {1, 2},
                                {3, 4},
                                {5, 6}
                            };
    for(int i = 0; i < 3; i++)
    {
        for(int j = 0; j < 2; j++)
        {
            cout << numberGrid[i][j];
        }
    }
    */

    //Pointers
    /*
    int age = 20;
    int *pAge = &age;
    cout << "Age is: " << *pAge << " And Pointer is: " << pAge;
    */

    //Class
    Book book1("Titlino","Mohamad ali",50);
    book1.CheckFunction();



    return 0;
}
