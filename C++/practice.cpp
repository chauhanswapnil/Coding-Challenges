#include <iostream>

using namespace std;

int main()
{

    // String data type
    /* */
    string name = "Swapnil Chauhan";

    cout << name[2] << endl;

    // Gives Index position the string starts at
    cout << name.find("Chauhan") << endl;

    // Output Chau
    cout << name.substr(8, 4) << endl;

    // Integer Data type
    int age;
    age = 24;

    double weight = 23.5;

    bool isAmazing = true;

    // Character data type
    char grade = 'A';

    cout << "Hi " << name << ". I am " << age << "years old." << endl;

    cout << "Size of char : " << sizeof(char) << endl;
    cout << "Size of int : " << sizeof(int) << endl;
    cout << "Size of long : " << sizeof(long) << endl;
    cout << "Size of float : " << sizeof(float) << endl;
    cout << "Size of double : " << sizeof(double) << endl;
    cout << "Size of double : " << sizeof(bool) << endl;

    return 0;
}
