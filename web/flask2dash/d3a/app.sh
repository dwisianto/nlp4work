


help(){

}

gt_br_orphan(){
    id=${FUNCNAME[0]}

    case "$@" in
        ${id} )
        echo "git switch --orphan a_branch_name" 
        ;;
    esac

}

acd_new(){
    id=${FUNCNAME[0]}

    case "$@" in
        ${id} )
        echo "conda create --name b39 python=3.9" 
        ;;
        ${id}_ )
        conda create --name b39 python=3.9
        ;;
    esac
}




clean(){
    id=${FUNCNAME[0]}

    case "$@" in
        ${id} )
        echo "find ./ -name '__pycache__' -exec rm -rf {} \; " 
        ;;
        ${id}- )
        find ./ -name '__pycache__' -exec rm -rf {} \;
        find ./ -name 'migrations' -exec rm -rf  {} \;
        ;;
    esac
}


pi_inst_rew(){
    id=${FUNCNAME[0]}
    
    case "$@" in
        ${id} )
        echo "pip install -r requirements.txt" 
        ;;
    esac
}


#
# flask db init
# flask db upgrade
# flask run --host=0.0.0.0
main(){
    clean "$@"
}
main "$@"


