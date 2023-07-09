

run(){
    eval "flask run"
}

acd_pip(){
    eval "pip install -r requirements"
}

main(){
    run "$@"
}
main "$@"