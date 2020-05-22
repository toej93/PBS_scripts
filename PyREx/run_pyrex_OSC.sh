#/bin/bash
#PBS -l nodes=1:ppn=40
#PBS -j oe
#PBS -A PCON0003
#PBS -m e
#PBS -l mem=128000MB
#PBS -l walltime=06:20:00

source /users/PCON0003/cond0068/.bash_profile_pitzer_cvmfs
module load python/3.6-conda5.2
export HDF5_USE_FILE_LOCKING=FALSE

cd $RUN_DIR

j=0
while [ $j -lt $MAX_JOBS ]
do
    END=$[$j+40]
    for i in $(seq $j $END) #3785
    do
        echo $i
        python rno_g_simulation.py ${ENERGY} 1 --output $TMPDIR/RNO_out_${ENERGY}_$j.hdf5 --noiseless -n ${EVSNUM} &
    done
    wait
    j=$[$j+40]
    pbsdcp $TMPDIR/'*' $OUTPUT_DIR
    rm $TMPDIR/*
done
