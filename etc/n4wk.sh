#!/bin/bash

#
# dev, data, acd
#
branch_id=101
declare -A branches=(
    [101new]=wk_dev_june6
    [101old]=dev
    [101dev]=dev
    [101raw]=main
    [101acd]=acd
    [101web]=web
    [101etc]=etc
    [101wiki]=wiki
)

declare -A origin=(
    [new]=${branches[${branch_id}old]}
    [old]=${branches[${branch_id}old]}
    [raw]=${branches[${branch_id}raw]}
    [dev]=${branches[${branch_id}dev]}
    [acd]=${branches[${branch_id}acd]}
    [web]=${branches[${branch_id}web]}
    [etc]=${branches[${branch_id}etc]}
    [wiki]=${branches[${branch_id}wiki]}
)

declare -A sandbox=(
    [new]=${branches[${branch_id}new]}
    [old]=${branches[${branch_id}old]}
    [raw]=${branches[${branch_id}raw]}
    [dev]=${branches[${branch_id}dev]}
    [acd]=${branches[${branch_id}acd]}
    [etc]=${branches[${branch_id}etc]}
    [wiki]=${branches[${branch_id}wiki]}
)


#
#
#
n4wk_repo='git@github.com:dwisianto/nlp4work.git'
git_repo=$n4wk_repo
git_wiki='git@github.com:dwisianto/nlp4work.wiki.git'

#
#
#
n4(){
    id=${FUNCNAME[0]}

    case "$@" in
        ${id} )
            echo " # "
            echo " # arg       : $@ "
            echo " # id        : ${id} "
            echo " # repo      : ${git_repo}"
            echo " # "
            echo " # origin_new : <${origin[new]}>"
            echo -n " # sandbox_new : <${sandbox[new]}>" && [ -d ${sandbox[new]} ] && echo "[exist]" || echo "[missing]"
            echo " # "
            echo " # origin_old : <${origin[old]}>"
            echo " # sandbox_old : <${sandbox[old]}>"
            echo " # "
            echo " # origin_wiki : <${origin[wiki]}>"
            echo " # sandbox_wiki : <${sandbox[wiki]}>"
            echo " # "
            ;;
        ${id}- )
            rm -rf ${sandbox[new]} && mkdir ${sandbox[new]}

            cd ${sandbox[new]} && git clone ${git_wiki} ${sandbox[wiki]} && cd ..
            cd ${sandbox[new]} && git clone --branch ${origin[etc]} --single-branch ${git_repo} ${sandbox[etc]} && cd ..		    
            cd ${sandbox[new]} && git clone --branch ${origin[dev]} --single-branch ${git_repo} ${sandbox[dev]} && cd .. 
            cd ${sandbox[new]} && git clone --branch ${origin[acd]]} --single-branch ${git_repo} ${sandbox[acd]} && cd .. 


            cd ${sandbox[new]} && \
            git clone --branch ${origin[new]} --single-branch ${git_repo} ${sandbox[new]} && \ 
            cd ${sandbox[new]} && \
            git checkout -b ${sandbox[new]} ${origin[new]} && \
            git push --set-upstream origin ${sandbox[new]} && \
            cd .. && \
            cd ..
            ;;
    esac
}



gt_br_orphan(){
    id=${FUNCNAME[0]}

    case "$@" in
        ${id} )
        echo "git switch --orphan a_branch_name" 
        ;;
    esac
}



main(){
    n4 "$@"
}

main "$@"