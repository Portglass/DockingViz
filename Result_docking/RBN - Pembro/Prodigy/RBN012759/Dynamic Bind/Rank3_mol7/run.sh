#!/bin/bash
# ===========================================================================
#    Automated script generated by the CSB server for PRODIGY-LIG execution
# ===========================================================================
# April 22, 2025 13:19:04 UTC
# ===========================================================================
outputfile="output.out"

echo "# ===========================================================================" &>>$outputfile
log="RBN012759_dynamic_bind_rank3_mol7.log"

cmd="prodigy_lig -c B X:UNK -i RBN012759_dynamic_bind_rank3_mol7.pdb -v"

echo "command: $cmd" &>>$outputfile
$cmd &>$log
status=$?
echo "exit status: $status" &>>$outputfile
echo "log:" &>>$outputfile
cat $log >>$outputfile

exit $status
# ===========================================================================