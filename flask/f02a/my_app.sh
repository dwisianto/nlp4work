#!/opt/homebrew/Cellar/bash/5.2.9/bin/bash

declare -A acd_=(
    [new]="conda create -n web903a --clone f9"
)

acd(){
    eval ${acd_[new]}
}

run(){
    eval "flask run"
}

acd_pip(){
    eval "pip install -r requirements"
}

main(){
    #run "$@"
    acd "$@"
}
main "$@"