# 파이썬 기초

> "Life is short, you need Python"

![파이썬](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQlN_pLp8zAqVRp6KqA20S2Lo0Q3lFv1ju3s7TfmtiFsgoRJQT)

## 0. 파이썬 설치

### 01. pyenv 설치

 1. [pyenv란?](https://github.com/pyenv/pyenv)

    * 여러 버전의 Python을 쉽게 **바꿔서 사용** 할 수 있게 해주는 도구

      

 2.  `pyenv` 설치 과정

    ``` shell
    $ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    
    $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    $ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
    $ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    
    $ exec $SHELL
    ```



## 1. 저장

### 1.1 변수

1. 파이썬에서 = 를 기준으로 오른쪽에 있는 값을 저장한다



### 1.2 자료형의 특징

| 문자 |    숫자     |   None   |   참/거짓    |
| :--: | :---------: | :------: | :----------: |
| str  | int / float | Nonetype | True / False |

