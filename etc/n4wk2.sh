#
# dev, data, acd
#
branch_id=101
declare -A branches=(
	[101new]=ds_dev_may4
	[101old]=dev
	[101raw]=main
	[101acd]=acd
    [604new]=ds_xlp_may
    [604old]=dev
    [604raw]=data
    [604acd]=acd
)
origin_new=${branches[${branch_id}old]}
sandbox_new=${branches[${branch_id}new]}

origin_raw=${branches[${branch_id}raw]}
sandbox_raw=ds_${origin_raw}

origin_acd=${branches[${branch_id}acd]}
sandbox_acd=ds_${origin_acd}
tcr_wiki=${branches[211]}

#
#
#
tcr_repo=git@git.oit.prdoit-cuse1.aces.sec.gov:arg/tcr-analytics.git
tcr_wiki_repo=git@git.oit.prdoit-cuse1.aces.sec.gov:arg/tcr-analytics.wiki.git


xlp(){
  id=${FUNCNAME[0]}

  case "$@" in
	  ${id} )
	    echo " # "
	    echo " # arg       : $@ "
	    echo " # id        : ${id} "
	    echo " # repo      : ${xcl_repo}"
	    echo " # "
	    echo " # origin_new : <${origin_new}>"
	    echo -n " # sandbox_new : <${sandbox_new}>" && [ -d ${sandbox_new} ] && echo "[exist]" || echo "[missing]"
	    echo " # "
	    echo " # origin_raw : <${origin_raw}>"
	    echo " # sandbox_raw : <${sandbox_raw}>"
	    echo " # "
	    echo " # origin_acd : <${origin_acd}>"
	    echo " # sandbox_acd : <${sandbox_acd}>"
	    echo " # "
	    ;;
	  ${id}- )
		    rm -rf ${sandbox_new} && mkdir ${sandbox_new}
		    cd ${sandbox_new} && git clone ${xcl_repo} ${sandbox_new}
		    
			cd ${sandbox_new} && \
		    git checkout ${origin_new} && \
		    git checkout -b ${sandbox_new} ${origin_new} && \
		    git push --set-upstream origin ${sandbox_new} && \
			cd .. && cd .. 

		    cd ${sandbox_new} && git clone --branch ${origin_raw} --single-branch ${xcl_repo} ${sandbox_raw} && cd ..		    
			cd ${sandbox_new} && git clone --branch ${origin_acd} --single-branch ${xcl_repo} ${sandbox_acd} && cd ..

	    ;;
  esac
}


tcr(){
	id=${FUNCNAME[0]}

	repo_origin=${tcr_repo}
	case "$@" in
		${id} )
			echo " # "
			echo " # arg       : $@ "
			echo " # id        : ${id} "
			echo " # repo      : ${repo_origin}"
			echo " # "
			echo " # origin_new : <${origin_new}>"
			echo -n " # sandbox_new : <${sandbox_new}>" && [ -d ${sandbox_new} ] && echo "[exist]" || echo "[missing]"
			echo " # "
			echo " # origin_raw : <${origin_raw}>"
			echo " # sandbox_raw : <${sandbox_raw}>"
			echo " # "
			echo " # origin_acd : <${origin_acd}>"
			echo " # sandbox_acd : <${sandbox_acd}>"
			echo " # "
			;;
		${id}- )
				rm -rf ${sandbox_new} && mkdir ${sandbox_new}
				cd ${sandbox_new} && git clone ${repo_origin} ${sandbox_new}
				
				cd ${sandbox_new} && \
				git checkout ${origin_new} && \
				git checkout -b ${sandbox_new} ${origin_new} && \
				git push --set-upstream origin ${sandbox_new} && \
				cd .. && cd .. 

				cd ${sandbox_new} && git clone --branch ${origin_raw} --single-branch ${xcl_repo} ${sandbox_raw} && cd ..		    
				cd ${sandbox_new} && git clone --branch ${origin_acd} --single-branch ${xcl_repo} ${sandbox_acd} && cd ..
			;;
	esac
}



acd(){
  id=${FUNCNAME[0]}

  case "$@" in
	  ${id} )
        echo "git checkout --orphan acd_dash38"
	    ;;
	  ${id}- )
        echo "git checkout --orphan acd_dash38"
	    ;;
  esac
}

vis(){
    id=${FUNCNAME[0]}

    case "$@" in
	${id} )
	    echo id:  ${id}
	    echo arg: "$@"
	    echo vis_repo: "${vis_repo}"
	    echo 'branch <new><old><raw>':"<${branch_new}> <${branch_old}> <${branch_raw}>"
	    echo "git clone vis_repo branch_new"
	    ;;
	${id}- )
	    git clone ${vis_repo} ${branch_new}
	    ;;
    esac
}


tcr-wiki(){
    id=${FUNCNAME[0]}

    case "$@" in 
	${id} )
	    echo "$@"
	    echo ${id}
	    echo "<${branch_new}> <${branch_old}> <${branch_raw}>"
	    echo "${tcr_wiki_repo}"
	    echo "git clone ${tcr_wiki_repo} ${tcr_new}"
	    ;;
	${id}- )
	    git clone ${tcr_wiki_repo} ${tcr_new}
	    ;;
    esac
}


main(){
    xlp "$@"
	tcr "$@"
	tcr-wiki "$@"
}
main "$@"