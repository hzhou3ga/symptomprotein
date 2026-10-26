to reproduce our results:

OS required: linux/unix with tcsh shell & python installed, python package scikit-learn (https://scikit-learn.org/) must also be installed 

modify the script 
scan_all_jkn_boostrf_top1_ent_null_knowgene.job
scan_all_jkn_boostrf_top1_ent_null_knowgene_tr.job
to point the variable PYTHON to the python version that you installed scikit-learn

Our whole prediction results are in 
all_side_qlt0.05new_hasgn_inclnovel_genelst.tsv 


####
4222 genes with known symptoms are in 
all_omim-3-side-3_qlt0.05new_mat_gn.lst

all symptoms having genes are in
all_side_qlt0.05new_hasgn_name.lst


feature and label vectors are
all_gn_qlt0.05new_all3fea.txt.gz  feature vector of 4222 genes
all_gn_noqlt0.05new_all3fea.txt.gz feature vector for 14187 genes not having known symptom
all_gn_qlt0.05new_label_0.txt.gz label vector for 4222 genes




####
to predict gene to symptoms with leave one out:
#### important ####
#### if you do not have computer cluster to do this, it will take around 4000 days to finish all  4222 genes on single node ####
#### because for each gene, one  has to train a model that take ~ 1 day on single node                       ####
#### thus, if you want to try this, use computer cluster by submitting the jobs to cluster !!!               ####


first run 'gzip -d *gz' to uncompress the *gz  files
then
generate SVM vector of the label vector

cat all_gn_qlt0.05new_label_0.txt | awk '{c="0";for(l=1;l<=7152;l++) c=c " " l ":" $l;print c,"#",$NF}' > all_gn_qlt0.05new_svmlabel.txt 

to predict symptoms for the 4222 training genes:

./scan_all_jkn_boostrf_top1_ent_null_knowgene.job

####
to predict symptoms for novel genes:
this will take ~24 hours

./scan_all_jkn_boostrf_top1_ent_null_knowgene_tr.job


####

merge gene-symptom predictions for getting symptom to gene predictions:
./scan_all_jkn_boostrf_top1_ent_null_knowgene_kn.job
--> all_sym2gn_pred.out
./scan_all_sym2gn_rr.job
--> get for symptom to gene predictions

add predicted precisions

./scan_all_predsym2gn_precision.job 

####
