#!/bin/bash




#
# dev, data, acd
#
branch_id=101
declare -A branches=(
	[101new]=n4wk_dev_may4
	[101old]=dev
    [101dev]=dev
	[101raw]=main
	[101acd]=acd
    [101etc]=etc
    [101wiki]=wiki
)
origin_new=${branches[${branch_id}old]}
sandbox_new=${branches[${branch_id}new]}

origin_dev=${branches[${branch_id}dev]}
sandbox_dev=${origin_dev}

origin_raw=${branches[${branch_id}raw]}
sandbox_raw=${origin_raw}

origin_acd=${branches[${branch_id}acd]}
sandbox_acd=${origin_acd}

origin_etc=${branches[${branch_id}etc]}
sandbox_etc=${origin_etc}


origin_wiki=${branches[${branch_id}wiki]}
sandbox_wiki=${origin_wiki}

#
#
#
n4wk_repo='git@github.com:dwisianto/nlp4work.git'
git_repo=$n4wk_repo
git_wiki='https://github.com/dwisianto/nlp4work.wiki.git'


n4_ops(){
    uid=${FUNCNAME[0]}

    sandbox_name="n4wk"
    dev_uid="dev"
    echo "rm -rf $sandbox_name && mkdir ${sandbox_name}"
    echo "cd ${sandbox_name} && git clone ${git_repo} --branch ${dev_uid} --single-branch ds_${dev_uid}"
}

n4_wiki(){
    uid=${FUNCNAME[0]}

    sandbox_name="n4wk"
    dev_uid="dev"
    echo "rm -rf $sandbox_name && mkdir ${sandbox_name}"
    echo "cd ${sandbox_name} && git clone ${git_repo} --branch ${dev_uid} --single-branch ds_${dev_uid}"

}



n4(){
    id=${FUNCNAME[0]}

    case "$@" in
        ${id} )
            echo " # "
            echo " # arg       : $@ "
            echo " # id        : ${id} "
            echo " # repo      : ${git_repo}"
            echo " # "
            echo " # origin_new : <${origin_new}>"
            echo -n " # sandbox_new : <${sandbox_new}>" && [ -d ${sandbox_new} ] && echo "[exist]" || echo "[missing]"
            echo " # "
            echo " # origin_raw : <${origin_raw}>"
            echo " # sandbox_raw : <${sandbox_raw}>"
            echo " # "
            echo " # origin_wiki : <${origin_wiki}>"
            echo " # sandbox_wiki : <${sandbox_wiki}>"
            echo " # "
            ;;
        ${id}- )
            rm -rf ${sandbox_new} && mkdir ${sandbox_new}
            cd ${sandbox_new} && git clone ${git_repo} ${sandbox_new} && cd .. 
            cd ${sandbox_new} && git clone --branch ${origin_etc} --single-branch ${git_repo} ${sandbox_etc} && cd ..		    
            cd ${sandbox_new} && git clone --branch ${origin_dev} --single-branch ${git_repo} ${sandbox_dev} && cd .. 
            #cd ${sandbox_new} && \
            #git checkout ${origin_new} && \
            #git checkout -b ${sandbox_new} ${origin_new} && \
            #git push --set-upstream origin ${sandbox_new} && \
            #cd .. && \
            #cd ..
            ;;
    esac
}




main(){
    n4 "$@"
    #n4_ops "$@"
    #n4_wiki "$@"
}

main "$@"