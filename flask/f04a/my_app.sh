
declare -A acd_=(
    [new]="conda create -n web902a --clone f9"
)
acd(){
    echo ${acd_[new]}
}

run(){
    eval "flask run"
}

acd_pip(){
    eval "pip install -r requirements"
}

main(){
    run "$@"
    acd "$@"
}
main "$@"