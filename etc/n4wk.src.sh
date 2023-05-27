#!/bin/bash


n4wk_repo='git@github.com:dwisianto/nlp4work.git'
git_repo=$n4wk_repo



n4-ops(){
    uid=${FUNCNAME[0]}

    sandbox_name="n4wk"
    dev_uid="dev"
    echo "rm -rf $sandbox_name && mkdir ${sandbox_name}"
    echo "cd ${sandbox_name} && git clone ${git_repo} --branch ${dev_uid} --single-branch ds_${dev_uid}"
}




main(){
    n4-ops "$@"
}

main "$@"