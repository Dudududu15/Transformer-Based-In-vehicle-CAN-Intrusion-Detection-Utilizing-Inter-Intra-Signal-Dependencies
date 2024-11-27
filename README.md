# Transformer-Based-In-vehicle-CAN-Intrusion-Detection-Utilizing-Inter-Intra-Signal-Dependencies
The code includes the intrusion detection part and the data reverse algorithm part. In the data reverse algorithm part, we have implemented the CCRE and READ algorithms.
Please note that if you are using your own dataset, it should include the "time" column, "dlc" column, "data" column, "label" column, and "id" column.
Currently, the data part that I have uploaded is normal data and fuzzing data.

How to run CCRE

--data
candata
--root_path
./dataset
--data_path
civic.csv
--method
CCRE


How to run CANformer


--is_training 1
--root_path ./dataset/civic/
--data_path fuzzing_final.csv
--data CAN
--model_id fuzzing
--model CANformer
--features M
--seq_len 192
--pred_len 96
--e_layers 2
--d_model 128
--d_ff 128
--factor 3
--e_layers 3
--enc_in 76
--c_out 76
--top_k 3
--anomaly_ratio 1
--batch_size 128
--train_epochs 5
