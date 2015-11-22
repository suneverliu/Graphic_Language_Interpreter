#include "tokenizer.h"

int main(int argc, char* argv[]) {
    Token token;

    if (argc < 2) {
        cout << "please input Source File !\n";

        return 0;
    }

    if (!init_tokenizer(argv[1])) return 0;

    cout << "记号类别    字符串      常数值      函数指针\n";
    cout << "____________________________________________\n";
    while(1) {
        token = get_token();
        if(token.type != NONTOKEN)
           cout << token.type << token.lexeme << token.value << token.FuncPtr;
        else
            break;
    };

    printf("____________________________________________\n");
    close_tokenizer();

    return 0;
}
