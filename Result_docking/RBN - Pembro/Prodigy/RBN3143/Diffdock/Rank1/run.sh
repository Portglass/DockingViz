#!/bin/bash
# ===========================================================================
#    Automated script generated by the CSB server for PRODIGY-LIG execution
# ===========================================================================
# April 22, 2025 12:02:20 UTC
# ===========================================================================
outputfile="output.out"

echo "# ===========================================================================" &>>$outputfile
log="RBN3143_Diffdock_protein__rank1_Chain_ligand_X.log"

cmd="prodigy_lig -c B X:UNK -i RBN3143_Diffdock_protein__rank1_Chain_ligand_X.pdb -v"

echo "command: $cmd" &>>$outputfile
$cmd &>$log
status=$?
echo "exit status: $status" &>>$outputfile
echo "log:" &>>$outputfile
cat $log >>$outputfile

exit $status
# ===========================================================================