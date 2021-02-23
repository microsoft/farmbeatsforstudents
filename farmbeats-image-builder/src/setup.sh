#!/bin/bash

INTERACTIVE=True
for i in $*
do
  case $i in
  --noninteractive)
    INTERACTIVE=False
    ;;
  *)
    # unknown option
    ;;
  esac
done

header() {
    printf "\n"
    echo "##################################################"
    echo "###     ${1}"
    echo "##################################################"
    printf "\n"
}

comment() {
    printf "\n"
    echo "###     ${1}"
}
