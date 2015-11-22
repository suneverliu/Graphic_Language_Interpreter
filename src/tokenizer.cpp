//
// Created by Sunever Liu on 2015/11/21.
//

#include "tokenizer.h"

ifstream input;


bool init_tokenizer(string filename) {
    try {
        input.open(filename, ios::in);
        if (!input)
            throw FileOpenError();
    } catch(FileOpenError e) {
        cerr << e << endl;
        return;
    }

    return true;
}

Token get_token() {
    string tokenBuffer = "";
    string character = "";
    Token token = {ERRTOKEN, "", 0.0, NULL};
    token.lexeme = tokenBuffer;

    input.read(character, 1);

    while(character[0] < 30) {
        input.read(character, 1);
    }

    tokenBuffer = tokenBuffer + character;

    input >> tokenBuffer;

    if (isalpha(character[0])) {
        input.read(character, 1);
        while(isalpha(character[0])){
            input.read(character, 1);
            tokenBuffer = tokenBuffer + character;
        }
        for(Token &t : TokenTab) {
            if (t.lexeme == tokenBuffer)
                return t;
        }

    }
    else if(isdigit(tokenBuffer[0])) {
        input.read(character, 1);
        while(isalpha(character[0])){
            input.read(character, 1);
            tokenBuffer = tokenBuffer + character;
        }
        token.type = CONST_ID;
        token.lexeme = tokenBuffer;
        istringstream iss(tokenBuffer);
        iss >> token.value;

        return token;
    }
    else {
        switch(character[0]) {
            case '*':
                input.read(character, 1);
                if(character[0] != '*') {
                    token.type = MUL;
                    token.lexeme = "*";
                }
                else {
                    token.type = POWER;
                    token.lexeme = "**";
                }
                return token;
            case '/':
                input.read(character, 1);
                if(character[0] != '/') {
                    token.type = DIV;
                    token.lexeme = "/";
                }
                else input.getline();
                return token;
            case '-':
                input.read(character, 1);
                if(character[0] != '-') {
                    token.type = MINUS;
                    token.lexeme = "-";
                }
                else input.getline();
                return token;
            case '+':
                token.type = PLUS;
                token.lexeme = "+";
                return token;
            case ',':
                token.type = COMMA;
                token.lexeme = ",";
                return token;
            case ';':
                token.type = SEMICO;
                token.lexeme = ";";
                return token;
            case '(':
                token.type = L_BRACKET;
                token.lexeme = "(";
                return token;
            case ')':
                token.type = R_BRACKET;
                token.lexeme = ")";
                return token;

        }
    }

    return token;
}

void close_tokenizer() {
    input.close();
}
