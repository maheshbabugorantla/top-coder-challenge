# Features order: trip_duration_days, miles_traveled, total_receipts_amount, miles_per_day, spend_per_day, miles_bucket, receipts_bucket, miles_per_day_bucket, receipt_cents, spend_per_day_bucket
def score(input):
    if input[2] < 841.11:
        if input[1] < 569.0:
            if input[2] < 23.47:
                if input[1] < 80.0:
                    var0 = 6.6457148
                else:
                    var0 = 16.642847
            else:
                if input[3] < 95.8:
                    var0 = 41.13262
                else:
                    var0 = 22.726604
        else:
            if input[3] < 206.25:
                if input[1] < 891.0:
                    var0 = 54.16743
                else:
                    var0 = 67.3203
            else:
                if input[2] < 519.94:
                    var0 = 33.849483
                else:
                    var0 = 47.55177
    else:
        if input[4] < 356.10333:
            if input[1] < 527.0:
                if input[2] < 1024.53:
                    var0 = 60.659023
                else:
                    var0 = 77.963326
            else:
                if input[8] < 99.0:
                    var0 = 90.419235
                else:
                    var0 = 29.14125
        else:
            if input[2] < 1072.44:
                var0 = 49.268734
            else:
                var0 = 71.4656
    if input[2] < 841.11:
        if input[0] < 5.0:
            if input[1] < 566.0:
                if input[1] < 204.0:
                    var1 = 13.255485
                else:
                    var1 = 23.427378
            else:
                if input[2] < 519.94:
                    var1 = 32.052807
                else:
                    var1 = 44.931892
        else:
            if input[1] < 482.0:
                if input[0] < 9.0:
                    var1 = 34.133087
                else:
                    var1 = 44.707863
            else:
                if input[2] < 493.0:
                    var1 = 51.538727
                else:
                    var1 = 65.06261
    else:
        if input[0] < 6.0:
            if input[1] < 622.0:
                var1 = 60.544098
            else:
                var1 = 72.45947
        else:
            if input[1] < 697.0:
                var1 = 76.57858
            else:
                if input[8] < 99.0:
                    var1 = 89.07262
                else:
                    var1 = 15.38872
    if input[2] < 834.06:
        if input[0] < 5.0:
            if input[1] < 566.0:
                if input[2] < 587.38:
                    var2 = 16.325539
                else:
                    var2 = 30.015982
            else:
                if input[7] < 26.0:
                    var2 = 36.81407
                else:
                    var2 = 21.604963
        else:
            if input[1] < 482.0:
                if input[2] < 568.58:
                    var2 = 33.762905
                else:
                    var2 = 45.812572
            else:
                var2 = 56.000813
    else:
        if input[0] < 5.0:
            if input[2] < 1072.44:
                var2 = 44.616055
            else:
                var2 = 63.23603
        else:
            if input[1] < 527.0:
                if input[8] < 99.0:
                    var2 = 68.906586
                else:
                    var2 = 18.49831
            else:
                if input[8] < 99.0:
                    var2 = 81.51959
                else:
                    var2 = 15.004001
    if input[2] < 863.93:
        if input[1] < 625.0:
            if input[2] < 579.29:
                if input[2] < 23.47:
                    var3 = 11.81395
                else:
                    var3 = 28.685104
            else:
                if input[4] < 140.93857:
                    var3 = 46.453995
                else:
                    var3 = 30.307077
        else:
            if input[3] < 232.0:
                if input[2] < 493.0:
                    var3 = 46.703976
                else:
                    var3 = 59.300476
            else:
                if input[2] < 540.6:
                    var3 = 28.994165
                else:
                    var3 = 40.68591
    else:
        if input[4] < 526.6575:
            if input[1] < 636.0:
                if input[2] < 1024.53:
                    var3 = 51.829967
                else:
                    var3 = 67.995735
            else:
                if input[8] < 99.0:
                    var3 = 77.79143
                else:
                    var3 = 14.628901
        else:
            if input[2] < 1084.16:
                var3 = 37.534252
            else:
                var3 = 58.821533
    if input[2] < 841.11:
        if input[0] < 5.0:
            if input[1] < 566.0:
                if input[2] < 568.58:
                    var4 = 14.238962
                else:
                    var4 = 26.67932
            else:
                var4 = 30.900223
        else:
            if input[1] < 836.0:
                if input[1] < 263.0:
                    var4 = 29.696516
                else:
                    var4 = 40.62867
            else:
                var4 = 54.604717
    else:
        if input[0] < 6.0:
            if input[1] < 305.0:
                if input[2] < 1241.21:
                    var4 = 38.909767
                else:
                    var4 = 52.198524
            else:
                if input[8] < 99.0:
                    var4 = 59.466774
                else:
                    var4 = 15.591858
        else:
            if input[1] < 697.0:
                if input[4] < 68.04667:
                    var4 = 16.740103
                else:
                    var4 = 65.34505
            else:
                if input[8] < 99.0:
                    var4 = 76.64612
                else:
                    var4 = 23.30757
    if input[2] < 863.93:
        if input[0] < 5.0:
            if input[1] < 566.0:
                if input[2] < 568.58:
                    var5 = 12.898221
                else:
                    var5 = 26.599665
            else:
                if input[2] < 519.94:
                    var5 = 26.692106
                else:
                    var5 = 37.362408
        else:
            if input[1] < 372.0:
                if input[0] < 9.0:
                    var5 = 25.950827
                else:
                    var5 = 36.237263
            else:
                if input[2] < 486.02:
                    var5 = 40.805824
                else:
                    var5 = 51.327583
    else:
        if input[0] < 5.0:
            if input[2] < 1072.44:
                var5 = 38.22645
            else:
                if input[1] < 72.0:
                    var5 = 30.605167
                else:
                    var5 = 54.21298
        else:
            if input[1] < 527.0:
                var5 = 59.94862
            else:
                if input[8] < 99.0:
                    var5 = 70.09804
                else:
                    var5 = 13.680489
    if input[2] < 863.93:
        if input[0] < 6.0:
            if input[1] < 566.0:
                if input[2] < 568.58:
                    var6 = 14.455253
                else:
                    var6 = 25.249464
            else:
                if input[2] < 540.6:
                    var6 = 27.655954
                else:
                    var6 = 39.33915
        else:
            if input[1] < 629.0:
                if input[2] < 519.94:
                    var6 = 30.697382
                else:
                    var6 = 40.742165
            else:
                var6 = 47.92866
    else:
        if input[0] < 6.0:
            if input[1] < 313.0:
                if input[2] < 1241.21:
                    var6 = 34.53787
                else:
                    var6 = 47.961456
            else:
                if input[8] < 99.0:
                    var6 = 54.127712
                else:
                    var6 = 14.246401
        else:
            if input[1] < 643.0:
                if input[2] < 974.73:
                    var6 = 42.34801
                else:
                    var6 = 59.814716
            else:
                if input[8] < 99.0:
                    var6 = 69.180565
                else:
                    var6 = 13.338477
    if input[2] < 863.93:
        if input[0] < 5.0:
            if input[5] < 11.0:
                if input[2] < 423.16:
                    var7 = 10.905701
                else:
                    var7 = 21.075052
            else:
                if input[2] < 540.6:
                    var7 = 24.022377
                else:
                    var7 = 35.60585
        else:
            if input[5] < 12.0:
                if input[2] < 568.58:
                    var7 = 27.202261
                else:
                    var7 = 38.615322
            else:
                if input[2] < 486.02:
                    var7 = 38.322536
                else:
                    var7 = 49.47257
    else:
        if input[0] < 6.0:
            if input[2] < 1072.44:
                var7 = 40.031647
            else:
                if input[3] < 17.5:
                    var7 = 31.488554
                else:
                    var7 = 51.296886
        else:
            if input[5] < 10.0:
                if input[4] < 68.04667:
                    var7 = 13.764185
                else:
                    var7 = 54.819183
            else:
                var7 = 64.59867
    if input[2] < 655.24:
        if input[0] < 5.0:
            if input[1] < 470.0:
                if input[0] < 3.0:
                    var8 = 5.215981
                else:
                    var8 = 15.425145
            else:
                if input[0] < 3.0:
                    var8 = 17.55083
                else:
                    var8 = 26.102613
        else:
            if input[1] < 836.0:
                if input[1] < 263.0:
                    var8 = 22.589342
                else:
                    var8 = 31.496662
            else:
                var8 = 42.040585
    else:
        if input[0] < 7.0:
            if input[2] < 1094.06:
                if input[1] < 368.0:
                    var8 = 29.601904
                else:
                    var8 = 40.37017
            else:
                if input[9] < 48.0:
                    var8 = 51.35326
                else:
                    var8 = 39.510334
        else:
            if input[1] < 500.0:
                if input[3] < 59.0:
                    var8 = 51.248318
                else:
                    var8 = 2.5109558
            else:
                var8 = 61.871998
    if input[2] < 834.06:
        if input[0] < 6.0:
            if input[1] < 569.0:
                if input[0] < 3.0:
                    var9 = 9.844016
                else:
                    var9 = 18.120327
            else:
                if input[2] < 540.6:
                    var9 = 23.491781
                else:
                    var9 = 34.227207
        else:
            if input[1] < 472.0:
                if input[0] < 10.0:
                    var9 = 23.317122
                else:
                    var9 = 31.034397
            else:
                if input[1] < 836.0:
                    var9 = 34.69082
                else:
                    var9 = 44.16519
    else:
        if input[0] < 6.0:
            if input[2] < 1084.16:
                var9 = 34.345787
            else:
                if input[7] < 43.0:
                    var9 = 46.24707
                else:
                    var9 = 13.497924
        else:
            if input[1] < 852.0:
                if input[8] < 99.0:
                    var9 = 52.548096
                else:
                    var9 = 17.414331
            else:
                var9 = 60.796223
    if input[2] < 655.24:
        if input[0] < 4.0:
            if input[1] < 470.0:
                if input[0] < 3.0:
                    var10 = 4.9373403
                else:
                    var10 = 12.285559
            else:
                if input[3] < 673.0:
                    var10 = 20.537321
                else:
                    var10 = 10.869113
        else:
            if input[1] < 629.0:
                if input[1] < 85.0:
                    var10 = 16.232471
                else:
                    var10 = 24.868853
            else:
                if input[4] < 149.13777:
                    var10 = 34.40206
                else:
                    var10 = 6.940717
    else:
        if input[0] < 7.0:
            if input[2] < 1084.16:
                if input[1] < 368.0:
                    var10 = 25.92887
                else:
                    var10 = 37.425045
            else:
                if input[4] < 1191.195:
                    var10 = 46.010796
                else:
                    var10 = 36.587826
        else:
            if input[1] < 483.0:
                if input[3] < 59.0:
                    var10 = 45.32635
                else:
                    var10 = 1.1344804
            else:
                var10 = 55.24411
    if input[2] < 863.93:
        if input[0] < 7.0:
            if input[1] < 289.0:
                if input[2] < 449.83:
                    var11 = 7.9130044
                else:
                    var11 = 18.510454
            else:
                if input[0] < 3.0:
                    var11 = 16.44412
                else:
                    var11 = 25.57342
        else:
            if input[1] < 805.0:
                if input[0] < 12.0:
                    var11 = 25.09757
                else:
                    var11 = 33.992573
            else:
                var11 = 40.771633
    else:
        if input[0] < 5.0:
            if input[2] < 1072.44:
                var11 = 26.921915
            else:
                if input[3] < 1068.0:
                    var11 = 40.08027
                else:
                    var11 = 19.173887
        else:
            if input[1] < 815.0:
                if input[0] < 11.0:
                    var11 = 42.550865
                else:
                    var11 = 51.207867
            else:
                var11 = 54.61086
    if input[2] < 735.52:
        if input[0] < 5.0:
            if input[1] < 456.0:
                if input[0] < 3.0:
                    var12 = 4.040333
                else:
                    var12 = 13.334331
            else:
                var12 = 19.483168
        else:
            if input[5] < 7.0:
                if input[4] < 140.13364:
                    var12 = 19.593948
                else:
                    var12 = 3.0070236
            else:
                if input[1] < 836.0:
                    var12 = 27.445526
                else:
                    var12 = 35.523296
    else:
        if input[0] < 5.0:
            if input[2] < 1072.44:
                if input[1] < 389.0:
                    var12 = 21.318079
                else:
                    var12 = 32.076504
            else:
                if input[1] < 72.0:
                    var12 = 19.588524
                else:
                    var12 = 37.697437
        else:
            if input[1] < 697.0:
                if input[2] < 1114.96:
                    var12 = 34.08341
                else:
                    var12 = 44.738426
            else:
                if input[8] < 99.0:
                    var12 = 51.082737
                else:
                    var12 = 6.963016
    if input[2] < 655.24:
        if input[0] < 6.0:
            if input[5] < 6.0:
                if input[0] < 3.0:
                    var13 = 3.7154367
                else:
                    var13 = 11.0046
            else:
                if input[0] < 3.0:
                    var13 = 12.039322
                else:
                    var13 = 20.915646
        else:
            if input[5] < 9.0:
                var13 = 20.808474
            else:
                if input[0] < 11.0:
                    var13 = 27.408426
                else:
                    var13 = 37.030148
    else:
        if input[0] < 7.0:
            if input[2] < 1072.44:
                if input[5] < 8.0:
                    var13 = 21.711163
                else:
                    var13 = 31.890497
            else:
                if input[5] < 4.0:
                    var13 = 29.582403
                else:
                    var13 = 39.301117
        else:
            if input[5] < 13.0:
                if input[2] < 1059.79:
                    var13 = 32.077293
                else:
                    var13 = 42.331142
            else:
                if input[8] < 99.0:
                    var13 = 48.973183
                else:
                    var13 = 13.1976385
    if input[2] < 651.64:
        if input[0] < 6.0:
            if input[1] < 566.0:
                if input[0] < 3.0:
                    var14 = 4.704732
                else:
                    var14 = 12.830234
            else:
                if input[7] < 26.0:
                    var14 = 19.261175
                else:
                    var14 = 10.681315
        else:
            if input[1] < 477.0:
                if input[1] < 85.0:
                    var14 = 12.734279
                else:
                    var14 = 20.736979
            else:
                if input[0] < 12.0:
                    var14 = 26.46984
                else:
                    var14 = 35.12354
    else:
        if input[0] < 6.0:
            if input[1] < 522.0:
                if input[2] < 1084.16:
                    var14 = 20.47546
                else:
                    var14 = 31.003513
            else:
                var14 = 36.155056
        else:
            if input[1] < 483.0:
                if input[2] < 967.0:
                    var14 = 27.825586
                else:
                    var14 = 39.02307
            else:
                if input[8] < 99.0:
                    var14 = 45.155117
                else:
                    var14 = 12.757717
    var15 = var0 + var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10 + var11 + var12 + var13 + var14
    if input[2] < 841.11:
        if input[0] < 6.0:
            if input[1] < 293.0:
                if input[2] < 456.24:
                    var16 = 6.6215014
                else:
                    var16 = 14.023851
            else:
                if input[0] < 2.0:
                    var16 = 10.297951
                else:
                    var16 = 19.64463
        else:
            if input[1] < 432.0:
                if input[1] < 76.0:
                    var16 = 13.417584
                else:
                    var16 = 21.215202
            else:
                if input[2] < 470.23:
                    var16 = 25.017736
                else:
                    var16 = 33.769318
    else:
        if input[0] < 5.0:
            if input[1] < 72.0:
                if input[1] < 47.0:
                    var16 = 21.558939
                else:
                    var16 = -8.954669
            else:
                if input[2] < 1070.22:
                    var16 = 22.48256
                else:
                    var16 = 32.705593
        else:
            if input[1] < 697.0:
                if input[0] < 11.0:
                    var16 = 32.8818
                else:
                    var16 = 42.224358
            else:
                if input[8] < 99.0:
                    var16 = 43.875164
                else:
                    var16 = 6.1400566
    if input[2] < 664.9:
        if input[0] < 7.0:
            if input[1] < 289.0:
                if input[0] < 2.0:
                    var17 = 1.3629135
                else:
                    var17 = 9.390895
            else:
                if input[0] < 3.0:
                    var17 = 11.094242
                else:
                    var17 = 18.45502
        else:
            if input[1] < 432.0:
                if input[1] < 85.0:
                    var17 = 12.405246
                else:
                    var17 = 19.394041
            else:
                if input[0] < 11.0:
                    var17 = 23.820204
                else:
                    var17 = 32.197968
    else:
        if input[1] < 483.0:
            if input[0] < 3.0:
                var17 = 19.587015
            else:
                if input[1] < 482.0:
                    var17 = 31.61121
                else:
                    var17 = -3.9320114
        else:
            if input[0] < 4.0:
                var17 = 30.123642
            else:
                if input[8] < 99.0:
                    var17 = 40.47255
                else:
                    var17 = 12.269724
    if input[6] < 15.0:
        if input[1] < 289.0:
            if input[0] < 3.0:
                if input[1] < 147.0:
                    var18 = 0.21725166
                else:
                    var18 = 5.554828
            else:
                if input[0] < 9.0:
                    var18 = 10.473907
                else:
                    var18 = 17.217958
        else:
            if input[0] < 5.0:
                if input[0] < 2.0:
                    var18 = 8.880321
                else:
                    var18 = 16.258883
            else:
                if input[0] < 11.0:
                    var18 = 21.686861
                else:
                    var18 = 28.582188
    else:
        if input[0] < 4.0:
            if input[1] < 622.0:
                if input[6] < 19.0:
                    var18 = 14.489601
                else:
                    var18 = 23.051756
            else:
                var18 = 29.510798
        else:
            if input[1] < 852.0:
                if input[0] < 11.0:
                    var18 = 30.583775
                else:
                    var18 = 37.059517
            else:
                var18 = 41.136093
    if input[2] < 793.55:
        if input[0] < 5.0:
            if input[1] < 159.0:
                if input[0] < 3.0:
                    var19 = 0.62910527
                else:
                    var19 = 6.502979
            else:
                if input[0] < 2.0:
                    var19 = 8.082488
                else:
                    var19 = 14.089759
        else:
            if input[1] < 629.0:
                if input[0] < 9.0:
                    var19 = 13.631925
                else:
                    var19 = 18.785255
            else:
                if input[2] < 493.0:
                    var19 = 21.610806
                else:
                    var19 = 29.29076
    else:
        if input[1] < 643.0:
            if input[0] < 10.0:
                if input[2] < 1422.11:
                    var19 = 22.19661
                else:
                    var19 = 28.123686
            else:
                if input[2] < 967.0:
                    var19 = 23.828451
                else:
                    var19 = 35.432404
        else:
            if input[3] < 206.25:
                if input[8] < 99.0:
                    var19 = 38.22559
                else:
                    var19 = 10.971901
            else:
                if input[7] < 43.0:
                    var19 = 29.984943
                else:
                    var19 = 11.026774
    if input[2] < 974.73:
        if input[0] < 4.0:
            if input[1] < 566.0:
                if input[2] < 519.94:
                    var20 = 4.6181393
                else:
                    var20 = 11.692628
            else:
                if input[2] < 540.6:
                    var20 = 13.048598
                else:
                    var20 = 19.781965
        else:
            if input[1] < 616.0:
                if input[2] < 579.29:
                    var20 = 14.165504
                else:
                    var20 = 21.026194
            else:
                if input[8] < 99.0:
                    var20 = 24.627184
                else:
                    var20 = 7.530998
    else:
        if input[0] < 5.0:
            if input[1] < 72.0:
                if input[1] < 47.0:
                    var20 = 16.036884
                else:
                    var20 = -10.98877
            else:
                if input[0] < 2.0:
                    var20 = 21.474771
                else:
                    var20 = 27.792343
        else:
            if input[1] < 891.0:
                if input[0] < 11.0:
                    var20 = 29.19325
                else:
                    var20 = 35.45712
            else:
                if input[4] < 150.28334:
                    var20 = 44.34168
                else:
                    var20 = 35.16969
    if input[2] < 655.24:
        if input[0] < 9.0:
            if input[1] < 191.0:
                if input[0] < 2.0:
                    var21 = -0.36609378
                else:
                    var21 = 6.4547496
            else:
                if input[0] < 3.0:
                    var21 = 8.137661
                else:
                    var21 = 15.522354
        else:
            if input[1] < 379.0:
                var21 = 15.811289
            else:
                if input[0] < 12.0:
                    var21 = 19.920126
                else:
                    var21 = 28.006977
    else:
        if input[0] < 11.0:
            if input[1] < 756.0:
                if input[2] < 1114.96:
                    var21 = 18.63745
                else:
                    var21 = 25.372604
            else:
                if input[3] < 815.0:
                    var21 = 31.448957
                else:
                    var21 = 19.035307
        else:
            if input[8] < 99.0:
                if input[1] < 229.0:
                    var21 = 28.542997
                else:
                    var21 = 35.653538
            else:
                var21 = 8.571957
    if input[2] < 841.11:
        if input[0] < 7.0:
            if input[1] < 293.0:
                if input[2] < 456.24:
                    var22 = 3.7643936
                else:
                    var22 = 10.03868
            else:
                if input[0] < 2.0:
                    var22 = 6.936641
                else:
                    var22 = 15.213599
        else:
            if input[1] < 616.0:
                if input[0] < 12.0:
                    var22 = 13.33357
                else:
                    var22 = 20.392035
            else:
                if input[2] < 423.16:
                    var22 = 20.779814
                else:
                    var22 = 27.893574
    else:
        if input[0] < 5.0:
            if input[1] < 313.0:
                if input[4] < 267.58:
                    var22 = 3.024431
                else:
                    var22 = 18.942612
            else:
                if input[0] < 2.0:
                    var22 = 19.1219
                else:
                    var22 = 26.260654
        else:
            if input[1] < 810.0:
                if input[0] < 12.0:
                    var22 = 25.497164
                else:
                    var22 = 32.41855
            else:
                if input[4] < 155.39333:
                    var22 = 37.3728
                else:
                    var22 = 30.904737
    if input[2] < 651.64:
        if input[0] < 9.0:
            if input[1] < 265.0:
                if input[0] < 2.0:
                    var23 = 0.746433
                else:
                    var23 = 6.871981
            else:
                if input[0] < 2.0:
                    var23 = 5.897172
                else:
                    var23 = 13.289803
        else:
            if input[1] < 872.0:
                if input[0] < 12.0:
                    var23 = 13.713979
                else:
                    var23 = 19.394836
            else:
                var23 = 24.330172
    else:
        if input[1] < 522.0:
            if input[0] < 3.0:
                if input[2] < 1404.28:
                    var23 = 11.43714
                else:
                    var23 = 16.52056
            else:
                if input[2] < 1241.21:
                    var23 = 19.190004
                else:
                    var23 = 25.665695
        else:
            if input[0] < 4.0:
                if input[2] < 1164.37:
                    var23 = 17.722322
                else:
                    var23 = 24.538069
            else:
                if input[1] < 989.0:
                    var23 = 28.39307
                else:
                    var23 = 33.54051
    if input[2] < 974.73:
        if input[0] < 5.0:
            if input[1] < 191.0:
                if input[0] < 2.0:
                    var24 = -0.578853
                else:
                    var24 = 5.3725457
            else:
                if input[2] < 568.58:
                    var24 = 8.804723
                else:
                    var24 = 13.951569
        else:
            if input[1] < 836.0:
                if input[0] < 11.0:
                    var24 = 12.7542925
                else:
                    var24 = 19.521275
            else:
                if input[2] < 475.95:
                    var24 = 17.595823
                else:
                    var24 = 26.206848
    else:
        if input[0] < 5.0:
            if input[1] < 72.0:
                if input[1] < 47.0:
                    var24 = 13.317116
                else:
                    var24 = -12.463574
            else:
                if input[4] < 267.58:
                    var24 = 8.08156
                else:
                    var24 = 21.946913
        else:
            if input[1] < 931.0:
                if input[0] < 13.0:
                    var24 = 25.203352
                else:
                    var24 = 31.83602
            else:
                if input[4] < 169.41692:
                    var24 = 36.500763
                else:
                    var24 = 27.817307
    if input[2] < 664.9:
        if input[0] < 6.0:
            if input[0] < 2.0:
                if input[1] < 534.0:
                    var25 = 0.5830197
                else:
                    var25 = 7.0818477
            else:
                if input[1] < 159.0:
                    var25 = 5.0844684
                else:
                    var25 = 10.476981
        else:
            if input[1] < 836.0:
                if input[1] < 89.0:
                    var25 = 7.469383
                else:
                    var25 = 14.565534
            else:
                var25 = 20.890808
    else:
        if input[0] < 5.0:
            if input[1] < 622.0:
                if input[0] < 2.0:
                    var25 = 11.448597
                else:
                    var25 = 17.200323
            else:
                if input[7] < 43.0:
                    var25 = 22.151754
                else:
                    var25 = 11.868369
        else:
            if input[1] < 822.0:
                if input[2] < 1241.21:
                    var25 = 19.120588
                else:
                    var25 = 25.275772
            else:
                if input[4] < 174.75:
                    var25 = 31.245014
                else:
                    var25 = 26.148672
    if input[2] < 974.73:
        if input[0] < 7.0:
            if input[2] < 568.58:
                if input[0] < 2.0:
                    var26 = 2.478866
                else:
                    var26 = 8.6851015
            else:
                if input[8] < 94.0:
                    var26 = 14.093757
                else:
                    var26 = -0.1692444
        else:
            if input[1] < 836.0:
                if input[0] < 12.0:
                    var26 = 12.137147
                else:
                    var26 = 17.988789
            else:
                if input[2] < 423.16:
                    var26 = 17.926645
                else:
                    var26 = 24.476744
    else:
        if input[4] < 174.75:
            if input[1] < 976.0:
                if input[0] < 10.0:
                    var26 = 19.148096
                else:
                    var26 = 26.993742
            else:
                var26 = 33.258186
        else:
            if input[1] < 566.0:
                if input[2] < 1422.11:
                    var26 = 12.950755
                else:
                    var26 = 19.789206
            else:
                if input[8] < 99.0:
                    var26 = 23.738232
                else:
                    var26 = 0.51563114
    if input[2] < 910.41:
        if input[0] < 6.0:
            if input[6] < 8.0:
                if input[1] < 472.0:
                    var27 = 3.2084386
                else:
                    var27 = 7.4515567
            else:
                if input[1] < 622.0:
                    var27 = 8.43775
                else:
                    var27 = 13.532916
        else:
            if input[1] < 836.0:
                if input[0] < 12.0:
                    var27 = 11.49182
                else:
                    var27 = 17.714785
            else:
                if input[9] < 5.0:
                    var27 = 20.488165
                else:
                    var27 = 5.4376616
    else:
        if input[0] < 11.0:
            if input[1] < 753.0:
                if input[2] < 1422.11:
                    var27 = 15.267097
                else:
                    var27 = 19.661755
            else:
                if input[0] < 2.0:
                    var27 = 15.497925
                else:
                    var27 = 24.08671
        else:
            if input[8] < 99.0:
                if input[0] < 13.0:
                    var27 = 24.17362
                else:
                    var27 = 29.062698
            else:
                var27 = 0.12647858
    if input[2] < 545.84:
        if input[0] < 9.0:
            if input[5] < 4.0:
                if input[0] < 2.0:
                    var28 = -0.71646434
                else:
                    var28 = 3.518596
            else:
                if input[0] < 3.0:
                    var28 = 4.753518
                else:
                    var28 = 10.122779
        else:
            if input[5] < 10.0:
                if input[3] < 0.875:
                    var28 = 2.2579668
                else:
                    var28 = 11.282607
            else:
                if input[0] < 12.0:
                    var28 = 14.41113
                else:
                    var28 = 20.365458
    else:
        if input[0] < 7.0:
            if input[6] < 28.0:
                if input[3] < 45.090908:
                    var28 = 8.263499
                else:
                    var28 = 14.486452
            else:
                if input[9] < 67.0:
                    var28 = 20.217676
                else:
                    var28 = 12.92968
        else:
            if input[0] < 13.0:
                if input[5] < 14.0:
                    var28 = 18.41263
                else:
                    var28 = 23.479368
            else:
                if input[3] < 6.090909:
                    var28 = 17.54284
                else:
                    var28 = 28.49055
    if input[2] < 664.9:
        if input[0] < 11.0:
            if input[5] < 6.0:
                if input[0] < 2.0:
                    var29 = 0.5325214
                else:
                    var29 = 5.404618
            else:
                if input[0] < 3.0:
                    var29 = 5.1756063
                else:
                    var29 = 11.045292
        else:
            if input[3] < 25.0:
                if input[3] < 0.875:
                    var29 = 2.2015169
                else:
                    var29 = 10.460353
            else:
                if input[8] < 99.0:
                    var29 = 18.709705
                else:
                    var29 = 3.8974671
    else:
        if input[0] < 6.0:
            if input[5] < 11.0:
                if input[8] < 54.0:
                    var29 = 10.294315
                else:
                    var29 = 15.714991
            else:
                if input[0] < 2.0:
                    var29 = 13.700801
                else:
                    var29 = 19.38442
        else:
            if input[5] < 19.0:
                if input[0] < 11.0:
                    var29 = 17.835903
                else:
                    var29 = 21.954407
            else:
                if input[2] < 1768.53:
                    var29 = 28.163742
                else:
                    var29 = 21.40194
    if input[2] < 974.73:
        if input[0] < 4.0:
            if input[1] < 566.0:
                if input[2] < 568.58:
                    var30 = 1.7728862
                else:
                    var30 = 6.6351943
            else:
                if input[2] < 475.95:
                    var30 = 6.8456864
                else:
                    var30 = 11.155833
        else:
            if input[2] < 486.02:
                if input[1] < 263.0:
                    var30 = 5.2172794
                else:
                    var30 = 11.184087
            else:
                if input[1] < 643.0:
                    var30 = 12.046155
                else:
                    var30 = 17.651361
    else:
        if input[0] < 5.0:
            if input[1] < 72.0:
                if input[0] < 4.0:
                    var30 = 9.535625
                else:
                    var30 = -14.331065
            else:
                if input[4] < 267.58:
                    var30 = -0.4157425
                else:
                    var30 = 16.034254
        else:
            if input[1] < 313.0:
                if input[2] < 1241.21:
                    var30 = 12.277003
                else:
                    var30 = 18.383154
            else:
                if input[4] < 153.15:
                    var30 = 25.833603
                else:
                    var30 = 20.270063
    if input[6] < 19.0:
        if input[0] < 8.0:
            if input[6] < 8.0:
                if input[0] < 2.0:
                    var31 = 0.05824228
                else:
                    var31 = 5.733008
            else:
                if input[8] < 95.0:
                    var31 = 10.230267
                else:
                    var31 = -0.6388883
        else:
            if input[1] < 872.0:
                if input[0] < 12.0:
                    var31 = 9.84999
                else:
                    var31 = 14.100899
            else:
                if input[6] < 9.0:
                    var31 = 14.545741
                else:
                    var31 = 21.154789
    else:
        if input[4] < 174.75:
            if input[1] < 904.0:
                if input[6] < 24.0:
                    var31 = 14.641083
                else:
                    var31 = 21.829315
            else:
                var31 = 26.272589
        else:
            if input[1] < 566.0:
                if input[4] < 176.572:
                    var31 = -1.5293
                else:
                    var31 = 14.822898
            else:
                if input[8] < 99.0:
                    var31 = 18.544218
                else:
                    var31 = -1.639061
    if input[2] < 974.73:
        if input[2] < 507.59:
            if input[5] < 5.0:
                if input[0] < 2.0:
                    var32 = -0.9124282
                else:
                    var32 = 4.0503087
            else:
                if input[0] < 11.0:
                    var32 = 7.271661
                else:
                    var32 = 13.969111
        else:
            if input[4] < 131.048:
                if input[8] < 99.0:
                    var32 = 15.376938
                else:
                    var32 = 1.0057678
            else:
                if input[8] < 99.0:
                    var32 = 9.584685
                else:
                    var32 = -2.0538461
    else:
        if input[0] < 5.0:
            if input[3] < 17.5:
                if input[2] < 2248.68:
                    var32 = 9.237168
                else:
                    var32 = -14.343361
            else:
                if input[0] < 2.0:
                    var32 = 11.010709
                else:
                    var32 = 15.139139
        else:
            if input[5] < 20.0:
                if input[0] < 13.0:
                    var32 = 16.749731
                else:
                    var32 = 21.866083
            else:
                if input[4] < 150.28334:
                    var32 = 26.980637
                else:
                    var32 = 20.03346
    if input[2] < 651.64:
        if input[0] < 3.0:
            if input[5] < 10.0:
                if input[3] < 439.02335:
                    var33 = 0.5595154
                else:
                    var33 = -4.576739
            else:
                if input[8] < 98.0:
                    var33 = 5.5443587
                else:
                    var33 = 0.2180008
        else:
            if input[0] < 12.0:
                if input[5] < 5.0:
                    var33 = 4.28497
                else:
                    var33 = 8.984533
            else:
                if input[3] < 4.9166665:
                    var33 = 4.3911242
                else:
                    var33 = 14.745877
    else:
        if input[5] < 10.0:
            if input[0] < 3.0:
                if input[2] < 1378.07:
                    var33 = 5.292301
                else:
                    var33 = 8.675713
            else:
                if input[2] < 1241.21:
                    var33 = 11.364686
                else:
                    var33 = 15.582791
        else:
            if input[0] < 13.0:
                if input[8] < 99.0:
                    var33 = 16.633192
                else:
                    var33 = -1.5255219
            else:
                var33 = 22.35116
    if input[2] < 974.73:
        if input[0] < 4.0:
            if input[1] < 566.0:
                if input[8] < 47.0:
                    var34 = 3.8707006
                else:
                    var34 = 0.6598984
            else:
                if input[2] < 608.92:
                    var34 = 6.4006915
                else:
                    var34 = 9.0788145
        else:
            if input[1] < 654.0:
                if input[0] < 12.0:
                    var34 = 7.113599
                else:
                    var34 = 12.048885
            else:
                if input[8] < 99.0:
                    var34 = 13.081716
                else:
                    var34 = 1.4394158
    else:
        if input[4] < 174.75:
            if input[1] < 976.0:
                if input[2] < 1191.4:
                    var34 = 13.536682
                else:
                    var34 = 18.856873
            else:
                if input[2] < 999.45:
                    var34 = 6.520566
                else:
                    var34 = 24.3039
        else:
            if input[1] < 198.0:
                if input[1] < 191.0:
                    var34 = 11.001971
                else:
                    var34 = -2.3094652
            else:
                if input[0] < 4.0:
                    var34 = 11.973052
                else:
                    var34 = 16.141167
    if input[2] < 517.54:
        if input[0] < 9.0:
            if input[1] < 191.0:
                if input[0] < 2.0:
                    var35 = -1.2940954
                else:
                    var35 = 2.274553
            else:
                if input[0] < 3.0:
                    var35 = 3.3178296
                else:
                    var35 = 6.818275
        else:
            if input[0] < 12.0:
                if input[3] < 42.5:
                    var35 = 5.2329493
                else:
                    var35 = 9.04544
            else:
                if input[1] < 41.0:
                    var35 = 3.7374084
                else:
                    var35 = 12.091056
    else:
        if input[0] < 6.0:
            if input[1] < 622.0:
                if input[2] < 1241.21:
                    var35 = 6.59518
                else:
                    var35 = 10.869899
            else:
                if input[7] < 12.0:
                    var35 = 15.110997
                else:
                    var35 = 11.199174
        else:
            if input[1] < 989.0:
                if input[2] < 1179.9:
                    var35 = 11.921734
                else:
                    var35 = 15.76547
            else:
                if input[2] < 1768.53:
                    var35 = 21.28849
                else:
                    var35 = 15.754491
    if input[2] < 716.7:
        if input[0] < 6.0:
            if input[1] < 472.0:
                if input[0] < 3.0:
                    var36 = -0.3866118
                else:
                    var36 = 4.1459546
            else:
                if input[8] < 98.0:
                    var36 = 6.674785
                else:
                    var36 = -0.37258607
        else:
            if input[1] < 379.0:
                if input[2] < 89.99:
                    var36 = 1.5436462
                else:
                    var36 = 6.5379844
            else:
                if input[0] < 11.0:
                    var36 = 9.062733
                else:
                    var36 = 13.82017
    else:
        if input[0] < 10.0:
            if input[1] < 622.0:
                if input[2] < 1422.11:
                    var36 = 7.8351398
                else:
                    var36 = 11.4345875
            else:
                if input[8] < 99.0:
                    var36 = 14.197118
                else:
                    var36 = -2.2822886
        else:
            if input[8] < 99.0:
                if input[0] < 13.0:
                    var36 = 14.67455
                else:
                    var36 = 18.926218
            else:
                if input[0] < 12.0:
                    var36 = 3.2987366
                else:
                    var36 = -2.7000108
    if input[2] < 519.94:
        if input[1] < 265.0:
            if input[0] < 9.0:
                if input[0] < 2.0:
                    var37 = -0.6720362
                else:
                    var37 = 2.069597
            else:
                if input[0] < 14.0:
                    var37 = 4.123658
                else:
                    var37 = 9.856168
        else:
            if input[0] < 11.0:
                if input[0] < 2.0:
                    var37 = 2.6272228
                else:
                    var37 = 6.4880614
            else:
                if input[8] < 16.0:
                    var37 = 3.9801698
                else:
                    var37 = 11.437198
    else:
        if input[1] < 483.0:
            if input[2] < 1422.11:
                if input[1] < 482.0:
                    var37 = 8.4377985
                else:
                    var37 = -12.940453
            else:
                if input[4] < 562.6275:
                    var37 = 14.244342
                else:
                    var37 = 7.6414843
        else:
            if input[0] < 4.0:
                if input[2] < 1164.37:
                    var37 = 7.1803527
                else:
                    var37 = 11.797922
            else:
                if input[8] < 99.0:
                    var37 = 15.298804
                else:
                    var37 = -0.046525575
    if input[2] < 910.41:
        if input[0] < 8.0:
            if input[5] < 5.0:
                if input[4] < 142.11667:
                    var38 = 1.4363375
                else:
                    var38 = 4.3525305
            else:
                if input[6] < 10.0:
                    var38 = 4.870093
                else:
                    var38 = 7.911751
        else:
            if input[5] < 19.0:
                if input[0] < 14.0:
                    var38 = 7.5420685
                else:
                    var38 = 13.393517
            else:
                var38 = 13.723198
    else:
        if input[4] < 174.75:
            if input[5] < 20.0:
                if input[2] < 1310.01:
                    var38 = 11.372476
                else:
                    var38 = 16.40165
            else:
                if input[2] < 1656.04:
                    var38 = 23.059084
                else:
                    var38 = 10.912852
        else:
            if input[5] < 6.0:
                if input[2] < 1246.48:
                    var38 = 3.178629
                else:
                    var38 = 9.626629
            else:
                if input[4] < 176.572:
                    var38 = -0.8885979
                else:
                    var38 = 12.358414
    if input[2] < 974.73:
        if input[0] < 4.0:
            if input[1] < 508.0:
                if input[2] < 587.38:
                    var39 = 0.40791264
                else:
                    var39 = 3.9618447
            else:
                if input[2] < 456.24:
                    var39 = 4.05788
                else:
                    var39 = 6.6227517
        else:
            if input[1] < 836.0:
                if input[0] < 13.0:
                    var39 = 6.185876
                else:
                    var39 = 11.440286
            else:
                if input[3] < 188.4:
                    var39 = 12.44077
                else:
                    var39 = 6.284648
    else:
        if input[0] < 4.0:
            if input[0] < 2.0:
                if input[1] < 483.0:
                    var39 = 3.6200242
                else:
                    var39 = 8.220353
            else:
                var39 = 10.025398
        else:
            if input[1] < 313.0:
                if input[3] < 65.77778:
                    var39 = 10.62281
                else:
                    var39 = -12.546395
            else:
                if input[4] < 150.28334:
                    var39 = 16.585884
                else:
                    var39 = 13.080589
    if input[2] < 555.49:
        if input[0] < 11.0:
            if input[1] < 147.0:
                if input[0] < 3.0:
                    var40 = -1.0206928
                else:
                    var40 = 1.9673313
            else:
                if input[4] < 111.9975:
                    var40 = 5.4117265
                else:
                    var40 = 3.0702524
        else:
            if input[4] < 40.83286:
                if input[1] < 452.0:
                    var40 = 7.5505443
                else:
                    var40 = 11.802337
            else:
                var40 = 4.437248
    else:
        if input[0] < 13.0:
            if input[1] < 643.0:
                if input[2] < 1422.11:
                    var40 = 6.769391
                else:
                    var40 = 10.114729
            else:
                if input[0] < 2.0:
                    var40 = 6.738065
                else:
                    var40 = 12.8174925
        else:
            if input[1] < 52.0:
                var40 = 6.88474
            else:
                var40 = 16.596874
    if input[2] < 507.59:
        if input[1] < 569.0:
            if input[0] < 3.0:
                if input[1] < 470.0:
                    var41 = -0.4950733
                else:
                    var41 = 2.6365588
            else:
                if input[1] < 85.0:
                    var41 = 0.80090934
                else:
                    var41 = 4.274733
        else:
            if input[0] < 7.0:
                if input[8] < 98.0:
                    var41 = 4.963975
                else:
                    var41 = -1.3249593
            else:
                if input[0] < 11.0:
                    var41 = 7.2275057
                else:
                    var41 = 10.812995
    else:
        if input[1] < 643.0:
            if input[0] < 12.0:
                if input[2] < 1422.11:
                    var41 = 5.852758
                else:
                    var41 = 9.234656
            else:
                if input[1] < 98.0:
                    var41 = 8.858306
                else:
                    var41 = 13.84568
        else:
            if input[8] < 99.0:
                if input[0] < 4.0:
                    var41 = 9.121364
                else:
                    var41 = 12.674219
            else:
                if input[0] < 9.0:
                    var41 = -3.2908552
                else:
                    var41 = 2.6188486
    if input[2] < 664.9:
        if input[1] < 472.0:
            if input[3] < 103.2:
                if input[1] < 112.0:
                    var42 = 0.71485555
                else:
                    var42 = 4.9456816
            else:
                if input[3] < 439.02335:
                    var42 = 0.46270943
                else:
                    var42 = -4.3065767
        else:
            if input[3] < 136.14285:
                if input[1] < 793.0:
                    var42 = 6.8863235
                else:
                    var42 = 10.433372
            else:
                if input[1] < 852.0:
                    var42 = 2.722646
                else:
                    var42 = 6.2630653
    else:
        if input[4] < 703.63336:
            if input[1] < 934.0:
                if input[2] < 1422.11:
                    var42 = 8.234604
                else:
                    var42 = 11.142526
            else:
                if input[4] < 174.75:
                    var42 = 15.30531
                else:
                    var42 = 11.174121
        else:
            if input[2] < 1815.6:
                if input[9] < 72.0:
                    var42 = 5.4901576
                else:
                    var42 = -17.377928
            else:
                if input[1] < 255.0:
                    var42 = 3.70796
                else:
                    var42 = 8.760127
    if input[6] < 19.0:
        if input[1] < 625.0:
            if input[0] < 4.0:
                if input[6] < 9.0:
                    var43 = 0.2849381
                else:
                    var43 = 2.788
            else:
                if input[6] < 6.0:
                    var43 = 2.514796
                else:
                    var43 = 5.5886035
        else:
            if input[0] < 7.0:
                if input[6] < 9.0:
                    var43 = 3.2226944
                else:
                    var43 = 6.4963837
            else:
                if input[4] < 16.933332:
                    var43 = 6.03618
                else:
                    var43 = 9.734153
    else:
        if input[0] < 5.0:
            if input[3] < 17.5:
                if input[1] < 32.0:
                    var43 = 6.351108
                else:
                    var43 = -16.666578
            else:
                if input[9] < 67.0:
                    var43 = 8.447579
                else:
                    var43 = 3.3235238
        else:
            if input[1] < 104.0:
                if input[1] < 9.0:
                    var43 = 1.2287018
                else:
                    var43 = 7.172245
            else:
                if input[4] < 150.28334:
                    var43 = 13.766734
                else:
                    var43 = 10.478916
    if input[6] < 11.0:
        if input[0] < 9.0:
            if input[1] < 147.0:
                if input[6] < 6.0:
                    var44 = -0.581641
                else:
                    var44 = 2.037674
            else:
                if input[0] < 3.0:
                    var44 = 1.9888328
                else:
                    var44 = 4.325038
        else:
            if input[1] < 1025.03:
                if input[0] < 14.0:
                    var44 = 4.580894
                else:
                    var44 = 10.33612
            else:
                if input[8] < 44.0:
                    var44 = 13.241304
                else:
                    var44 = 6.8616214
    else:
        if input[1] < 586.0:
            if input[0] < 11.0:
                if input[8] < 51.0:
                    var44 = 3.7220757
                else:
                    var44 = 7.444481
            else:
                if input[8] < 97.0:
                    var44 = 10.577647
                else:
                    var44 = -4.520421
        else:
            if input[3] < 356.5:
                if input[8] < 99.0:
                    var44 = 10.54168
                else:
                    var44 = -2.049012
            else:
                if input[6] < 15.0:
                    var44 = 0.37430725
                else:
                    var44 = 7.0494766
    if input[2] < 1013.03:
        if input[0] < 12.0:
            if input[1] < 678.0:
                if input[1] < 213.0:
                    var45 = 0.8677225
                else:
                    var45 = 3.6052854
            else:
                if input[2] < 540.6:
                    var45 = 5.082861
                else:
                    var45 = 7.9492683
        else:
            if input[2] < 486.02:
                if input[1] < 66.13:
                    var45 = 0.4210579
                else:
                    var45 = 7.5042114
            else:
                var45 = 10.899753
    else:
        if input[4] < 174.75:
            if input[1] < 1006.0:
                if input[2] < 1179.9:
                    var45 = 7.169192
                else:
                    var45 = 11.517055
            else:
                if input[2] < 1768.53:
                    var45 = 17.421715
                else:
                    var45 = 8.136319
        else:
            if input[4] < 176.572:
                var45 = -13.798186
            else:
                if input[0] < 2.0:
                    var45 = 4.0125647
                else:
                    var45 = 8.530383
    if input[2] < 974.73:
        if input[0] < 12.0:
            if input[5] < 5.0:
                if input[2] < 364.79:
                    var46 = 0.28498974
                else:
                    var46 = 3.1172462
            else:
                if input[0] < 2.0:
                    var46 = 1.3999316
                else:
                    var46 = 5.371566
        else:
            if input[8] < 97.0:
                if input[2] < 484.34:
                    var46 = 6.168698
                else:
                    var46 = 10.537982
            else:
                var46 = -4.679906
    else:
        if input[0] < 4.0:
            if input[7] < 43.0:
                if input[5] < 12.0:
                    var46 = 4.3392305
                else:
                    var46 = 7.3272433
            else:
                if input[2] < 1549.86:
                    var46 = 7.3680053
                else:
                    var46 = -17.303118
        else:
            if input[5] < 2.0:
                if input[4] < 562.6275:
                    var46 = 5.181082
                else:
                    var46 = -8.390998
            else:
                if input[0] < 13.0:
                    var46 = 9.300102
                else:
                    var46 = 12.751356
    if input[6] < 19.0:
        if input[0] < 7.0:
            if input[1] < 213.0:
                if input[1] < 210.0:
                    var47 = 0.9248498
                else:
                    var47 = -6.1950755
            else:
                if input[0] < 3.0:
                    var47 = 1.8304147
                else:
                    var47 = 4.3449483
        else:
            if input[1] < 793.0:
                if input[0] < 13.0:
                    var47 = 4.061241
                else:
                    var47 = 8.3430395
            else:
                if input[8] < 99.0:
                    var47 = 8.39018
                else:
                    var47 = 0.71303713
    else:
        if input[0] < 5.0:
            if input[3] < 17.5:
                if input[1] < 32.0:
                    var47 = 4.976898
                else:
                    var47 = -16.346449
            else:
                if input[6] < 37.0:
                    var47 = 4.789213
                else:
                    var47 = 7.8859134
        else:
            if input[1] < 586.0:
                if input[0] < 14.0:
                    var47 = 6.8968673
                else:
                    var47 = 12.432199
            else:
                if input[8] < 99.0:
                    var47 = 10.008037
                else:
                    var47 = -2.2035532
    if input[2] < 749.56:
        if input[0] < 6.0:
            if input[0] < 2.0:
                if input[1] < 534.0:
                    var48 = -1.2989753
                else:
                    var48 = 2.2313488
            else:
                if input[3] < 46.142857:
                    var48 = 0.6877545
                else:
                    var48 = 3.2735112
        else:
            if input[1] < 263.0:
                if input[2] < 373.98:
                    var48 = -0.013267635
                else:
                    var48 = 3.45036
            else:
                if input[0] < 11.0:
                    var48 = 4.980764
                else:
                    var48 = 8.284937
    else:
        if input[0] < 4.0:
            if input[9] < 71.0:
                if input[1] < 756.0:
                    var48 = 4.329526
                else:
                    var48 = 7.37199
            else:
                if input[1] < 993.0:
                    var48 = 5.016191
                else:
                    var48 = -16.99027
        else:
            if input[8] < 99.0:
                if input[1] < 104.0:
                    var48 = 4.502849
                else:
                    var48 = 8.851242
            else:
                var48 = -3.9619179
    if input[2] < 983.23:
        if input[1] < 629.0:
            if input[0] < 10.0:
                if input[2] < 373.98:
                    var49 = 0.726055
                else:
                    var49 = 2.9351327
            else:
                if input[8] < 99.0:
                    var49 = 5.0025325
                else:
                    var49 = -2.6879294
        else:
            if input[3] < 183.8:
                if input[2] < 545.84:
                    var49 = 4.790508
                else:
                    var49 = 7.562546
            else:
                if input[8] < 98.0:
                    var49 = 3.4989946
                else:
                    var49 = -1.8391113
    else:
        if input[4] < 153.15:
            if input[1] < 1014.0:
                if input[2] < 1179.9:
                    var49 = 6.1580195
                else:
                    var49 = 10.423161
            else:
                if input[2] < 999.45:
                    var49 = 1.5664704
                else:
                    var49 = 15.503903
        else:
            if input[1] < 553.0:
                if input[8] < 52.0:
                    var49 = 3.139424
                else:
                    var49 = 7.0441775
            else:
                if input[8] < 99.0:
                    var49 = 7.406791
                else:
                    var49 = -4.3732147
    if input[2] < 1013.03:
        if input[2] < 475.95:
            if input[1] < 1077.0:
                if input[1] < 265.0:
                    var50 = 0.75266564
                else:
                    var50 = 2.8371634
            else:
                if input[3] < 115.75:
                    var50 = 7.776905
                else:
                    var50 = 4.0977726
        else:
            if input[8] < 99.0:
                if input[4] < 415.78168:
                    var50 = 5.5848117
                else:
                    var50 = 1.3220485
            else:
                if input[4] < 51.16143:
                    var50 = 0.3683258
                else:
                    var50 = -5.499834
    else:
        if input[4] < 153.15:
            if input[1] < 1014.0:
                if input[2] < 1346.21:
                    var50 = 7.418808
                else:
                    var50 = 10.313772
            else:
                var50 = 15.308792
        else:
            if input[2] < 1114.96:
                if input[4] < 267.58:
                    var50 = -3.16199
                else:
                    var50 = 2.8159225
            else:
                if input[7] < 43.0:
                    var50 = 6.595121
                else:
                    var50 = -3.2107353
    if input[2] < 1013.03:
        if input[0] < 10.0:
            if input[1] < 763.0:
                if input[0] < 2.0:
                    var51 = -0.90295666
                else:
                    var51 = 2.465916
            else:
                if input[2] < 456.24:
                    var51 = 3.1761625
                else:
                    var51 = 5.4287076
        else:
            if input[1] < 965.0:
                if input[8] < 99.0:
                    var51 = 5.221059
                else:
                    var51 = -1.7359047
            else:
                if input[4] < 25.788:
                    var51 = 5.6794505
                else:
                    var51 = 10.963443
    else:
        if input[4] < 174.75:
            if input[7] < 4.0:
                if input[0] < 10.0:
                    var51 = 3.6229577
                else:
                    var51 = 8.74013
            else:
                if input[1] < 822.0:
                    var51 = 4.934135
                else:
                    var51 = 13.80275
        else:
            if input[2] < 1422.11:
                if input[8] < 50.0:
                    var51 = 0.17237346
                else:
                    var51 = 6.0058265
            else:
                if input[1] < 80.0:
                    var51 = 0.79944557
                else:
                    var51 = 6.614019
    if input[2] < 475.95:
        if input[1] < 94.0:
            if input[2] < 290.78:
                if input[4] < 2.850909:
                    var52 = 1.1547359
                else:
                    var52 = -1.8822596
            else:
                if input[0] < 9.0:
                    var52 = 0.17860794
                else:
                    var52 = 2.1994522
        else:
            if input[0] < 2.0:
                if input[2] < 171.32:
                    var52 = 0.53703195
                else:
                    var52 = -1.0237978
            else:
                if input[0] < 12.0:
                    var52 = 2.8345141
                else:
                    var52 = 5.7270627
    else:
        if input[0] < 13.0:
            if input[1] < 654.0:
                if input[2] < 1241.21:
                    var52 = 2.747751
                else:
                    var52 = 5.317132
            else:
                if input[3] < 356.5:
                    var52 = 7.0299845
                else:
                    var52 = 4.274509
        else:
            if input[8] < 98.0:
                if input[2] < 486.02:
                    var52 = 0.14793244
                else:
                    var52 = 9.818141
            else:
                var52 = -4.4243393
    if input[2] < 769.23:
        if input[0] < 5.0:
            if input[1] < 885.0:
                if input[0] < 2.0:
                    var53 = -0.43576726
                else:
                    var53 = 1.144932
            else:
                if input[7] < 14.0:
                    var53 = 4.4114385
                else:
                    var53 = 1.3259419
        else:
            if input[1] < 263.0:
                if input[3] < 41.5:
                    var53 = 1.8958822
                else:
                    var53 = -2.6737828
            else:
                if input[2] < 252.08:
                    var53 = 2.527882
                else:
                    var53 = 5.393742
    else:
        if input[1] < 313.0:
            if input[0] < 9.0:
                if input[8] < 50.0:
                    var53 = 0.9420473
                else:
                    var53 = 3.779597
            else:
                if input[2] < 1171.99:
                    var53 = 3.301757
                else:
                    var53 = 6.7004313
        else:
            if input[8] < 99.0:
                if input[0] < 4.0:
                    var53 = 4.3344603
                else:
                    var53 = 7.4009027
            else:
                var53 = -4.1632853
    if input[2] < 1013.03:
        if input[8] < 99.0:
            if input[1] < 147.0:
                if input[2] < 298.68:
                    var54 = -0.8748054
                else:
                    var54 = 1.8441445
            else:
                if input[0] < 4.0:
                    var54 = 2.2353194
                else:
                    var54 = 4.304662
        else:
            if input[2] < 631.88:
                if input[3] < 74.416664:
                    var54 = 0.31964234
                else:
                    var54 = -2.410832
            else:
                var54 = -5.5841675
    else:
        if input[0] < 4.0:
            if input[1] < 616.0:
                if input[0] < 2.0:
                    var54 = 0.23418322
                else:
                    var54 = 3.1818013
            else:
                if input[2] < 1815.6:
                    var54 = 3.6094136
                else:
                    var54 = 6.0929284
        else:
            if input[3] < 100.6:
                if input[0] < 13.0:
                    var54 = 5.2695365
                else:
                    var54 = 8.704265
            else:
                if input[4] < 169.41692:
                    var54 = 12.237515
                else:
                    var54 = 7.440718
    if input[2] < 517.54:
        if input[0] < 11.0:
            if input[1] < 147.0:
                if input[2] < 364.79:
                    var55 = -0.9824815
                else:
                    var55 = 1.5384601
            else:
                if input[1] < 885.0:
                    var55 = 1.5045849
                else:
                    var55 = 3.5635579
        else:
            if input[1] < 66.13:
                if input[1] < 41.0:
                    var55 = 0.82607806
                else:
                    var55 = -1.4406083
            else:
                if input[2] < 106.86:
                    var55 = 9.912791
                else:
                    var55 = 4.400588
    else:
        if input[0] < 3.0:
            if input[9] < 71.0:
                if input[1] < 508.0:
                    var55 = 0.66047585
                else:
                    var55 = 4.005585
            else:
                if input[1] < 993.0:
                    var55 = 1.7635721
                else:
                    var55 = -17.141226
        else:
            if input[8] < 99.0:
                if input[0] < 13.0:
                    var55 = 5.25718
                else:
                    var55 = 8.391439
            else:
                if input[2] < 631.88:
                    var55 = 0.7701538
                else:
                    var55 = -4.977403
    if input[6] < 15.0:
        if input[0] < 6.0:
            if input[1] < 472.0:
                if input[3] < 439.02335:
                    var56 = 0.5824023
                else:
                    var56 = -5.675283
            else:
                if input[8] < 91.0:
                    var56 = 2.5097463
                else:
                    var56 = -0.8538402
        else:
            if input[0] < 13.0:
                if input[1] < 210.0:
                    var56 = 0.4948686
                else:
                    var56 = 3.708636
            else:
                if input[4] < 36.452145:
                    var56 = 4.3185916
                else:
                    var56 = 9.604812
    else:
        if input[1] < 313.0:
            if input[0] < 12.0:
                if input[8] < 50.0:
                    var56 = 0.58130825
                else:
                    var56 = 3.4942677
            else:
                if input[1] < 98.0:
                    var56 = 3.948225
                else:
                    var56 = 7.3130975
        else:
            if input[8] < 99.0:
                if input[1] < 1100.0:
                    var56 = 5.3204055
                else:
                    var56 = 7.729776
            else:
                var56 = -4.181377
    if input[2] < 517.54:
        if input[1] < 200.0:
            if input[2] < 364.79:
                if input[3] < 21.142857:
                    var57 = -1.9797032
                else:
                    var57 = 0.2676456
            else:
                if input[3] < 24.09091:
                    var57 = 2.0851154
                else:
                    var57 = -0.523493
        else:
            if input[4] < 115.82:
                if input[8] < 99.0:
                    var57 = 2.8065689
                else:
                    var57 = -2.6923554
            else:
                if input[1] < 470.0:
                    var57 = -2.0444436
                else:
                    var57 = 1.486012
    else:
        if input[1] < 989.0:
            if input[8] < 99.0:
                if input[3] < 261.75:
                    var57 = 4.5708194
                else:
                    var57 = 1.7914473
            else:
                if input[2] < 631.88:
                    var57 = 0.42009684
                else:
                    var57 = -4.952034
        else:
            if input[3] < 206.25:
                if input[2] < 1734.56:
                    var57 = 9.637797
                else:
                    var57 = 5.753042
            else:
                if input[7] < 43.0:
                    var57 = 4.6340714
                else:
                    var57 = 0.33052725
    if input[2] < 568.58:
        if input[0] < 10.0:
            if input[1] < 625.0:
                if input[3] < 278.25:
                    var58 = 0.6980356
                else:
                    var58 = -2.3104331
            else:
                if input[2] < 314.81:
                    var58 = 1.0262605
                else:
                    var58 = 3.021389
        else:
            if input[3] < 89.0:
                if input[1] < 730.0:
                    var58 = 3.9320428
                else:
                    var58 = 0.72000426
            else:
                if input[3] < 115.75:
                    var58 = 7.4580903
                else:
                    var58 = 0.49439088
    else:
        if input[0] < 11.0:
            if input[1] < 756.0:
                if input[2] < 1448.55:
                    var58 = 1.7707036
                else:
                    var58 = 4.0819535
            else:
                if input[7] < 4.0:
                    var58 = 2.1049895
                else:
                    var58 = 5.569121
        else:
            if input[1] < 1096.0:
                if input[0] < 13.0:
                    var58 = 4.9367266
                else:
                    var58 = 7.055996
            else:
                if input[2] < 865.92:
                    var58 = -0.0028259277
                else:
                    var58 = 10.331752
    if input[2] < 1129.52:
        if input[1] < 836.0:
            if input[8] < 99.0:
                if input[0] < 14.0:
                    var59 = 1.7827307
                else:
                    var59 = 6.454023
            else:
                if input[2] < 545.84:
                    var59 = -0.7899575
                else:
                    var59 = -5.1214976
        else:
            if input[7] < 7.0:
                if input[2] < 672.91:
                    var59 = 4.6829233
                else:
                    var59 = 7.838894
            else:
                if input[2] < 1084.16:
                    var59 = 3.0574653
                else:
                    var59 = -1.1665528
    else:
        if input[4] < 153.15:
            if input[1] < 1014.0:
                if input[2] < 1820.8:
                    var59 = 5.8982024
                else:
                    var59 = 9.909204
            else:
                if input[2] < 1768.53:
                    var59 = 11.951476
                else:
                    var59 = 0.53576356
        else:
            if input[2] < 1422.11:
                if input[1] < 616.0:
                    var59 = -0.23937921
                else:
                    var59 = 4.249084
            else:
                if input[8] < 99.0:
                    var59 = 4.5270805
                else:
                    var59 = -4.497371
    if input[6] < 8.0:
        if input[0] < 6.0:
            if input[1] < 976.0:
                if input[4] < 89.18643:
                    var60 = 0.037127048
                else:
                    var60 = -1.1584172
            else:
                if input[1] < 1029.0:
                    var60 = 3.0125062
                else:
                    var60 = 0.6761589
        else:
            if input[1] < 85.0:
                if input[1] < 52.0:
                    var60 = 0.033582687
                else:
                    var60 = -2.8277853
            else:
                if input[0] < 13.0:
                    var60 = 2.2567937
                else:
                    var60 = 5.944002
    else:
        if input[1] < 756.0:
            if input[0] < 12.0:
                if input[6] < 22.0:
                    var60 = 1.4411488
                else:
                    var60 = 3.063012
            else:
                if input[8] < 98.0:
                    var60 = 5.5610504
                else:
                    var60 = -3.7656357
        else:
            if input[4] < 149.6:
                if input[1] < 1014.0:
                    var60 = 4.5315747
                else:
                    var60 = 8.462606
            else:
                if input[0] < 8.0:
                    var60 = 5.2364326
                else:
                    var60 = 2.8257487
    if input[0] < 10.0:
        if input[1] < 753.0:
            if input[1] < 72.0:
                if input[1] < 69.0:
                    var61 = -0.12906963
                else:
                    var61 = -11.33522
            else:
                if input[2] < 1880.69:
                    var61 = 1.2346308
                else:
                    var61 = 3.8706887
        else:
            if input[7] < 4.0:
                if input[0] < 9.0:
                    var61 = -5.398172
                else:
                    var61 = 0.4646454
            else:
                if input[2] < 999.45:
                    var61 = 2.6630101
                else:
                    var61 = 5.0248895
    else:
        if input[1] < 1025.03:
            if input[0] < 13.0:
                if input[2] < 1147.89:
                    var61 = 2.31574
                else:
                    var61 = 4.5738244
            else:
                if input[8] < 98.0:
                    var61 = 6.160215
                else:
                    var61 = -3.6714952
        else:
            if input[4] < 25.788:
                if input[0] < 14.0:
                    var61 = 2.735846
                else:
                    var61 = 0.6565104
            else:
                if input[2] < 2072.39:
                    var61 = 9.492871
                else:
                    var61 = 4.0405927
    if input[2] < 1129.52:
        if input[1] < 885.0:
            if input[0] < 3.0:
                if input[8] < 46.0:
                    var62 = 0.36504406
                else:
                    var62 = -1.4174236
            else:
                if input[8] < 99.0:
                    var62 = 2.0141509
                else:
                    var62 = -2.4662483
        else:
            if input[3] < 188.4:
                if input[2] < 664.9:
                    var62 = 4.0918765
                else:
                    var62 = 6.941457
            else:
                if input[8] < 28.0:
                    var62 = 3.2439175
                else:
                    var62 = 0.98808634
    else:
        if input[4] < 153.15:
            if input[4] < 143.48625:
                if input[1] < 1014.0:
                    var62 = 4.827741
                else:
                    var62 = 9.264365
            else:
                if input[1] < 1158.0:
                    var62 = 9.375617
                else:
                    var62 = 0.350708
        else:
            if input[1] < 1100.0:
                if input[7] < 43.0:
                    var62 = 3.2683513
                else:
                    var62 = -17.362907
            else:
                if input[8] < 87.0:
                    var62 = 6.301329
                else:
                    var62 = 2.6034436
    if input[2] < 999.45:
        if input[1] < 265.0:
            if input[2] < 407.43:
                if input[4] < 8.236:
                    var63 = 1.5817083
                else:
                    var63 = -0.91714716
            else:
                if input[8] < 99.0:
                    var63 = 1.9179529
                else:
                    var63 = -3.6113362
        else:
            if input[3] < 188.4:
                if input[1] < 1056.0:
                    var63 = 2.640166
                else:
                    var63 = 5.0171485
            else:
                if input[1] < 452.0:
                    var63 = -1.4822102
                else:
                    var63 = 1.4911126
    else:
        if input[1] < 210.0:
            if input[1] < 195.73:
                if input[4] < 492.1575:
                    var63 = 3.0708005
                else:
                    var63 = -1.1158929
            else:
                if input[4] < 245.9425:
                    var63 = -9.134601
                else:
                    var63 = 2.4585755
        else:
            if input[4] < 153.15:
                if input[3] < 95.4:
                    var63 = 5.4184732
                else:
                    var63 = 9.754515
            else:
                if input[4] < 1191.195:
                    var63 = 4.169486
                else:
                    var63 = 1.301679
    if input[0] < 11.0:
        if input[1] < 756.0:
            if input[8] < 48.0:
                if input[2] < 314.81:
                    var64 = -0.527766
                else:
                    var64 = 2.7032166
            else:
                if input[8] < 50.0:
                    var64 = -14.122054
                else:
                    var64 = 1.7680476
        else:
            if input[2] < 540.6:
                if input[7] < 14.0:
                    var64 = 1.6131499
                else:
                    var64 = 0.062086817
            else:
                if input[4] < 150.28334:
                    var64 = 6.129543
                else:
                    var64 = 3.5798929
    else:
        if input[0] < 13.0:
            if input[3] < 95.4:
                if input[2] < 2296.07:
                    var64 = 3.5455346
                else:
                    var64 = 0.9747483
            else:
                if input[2] < 271.93:
                    var64 = 1.1712312
                else:
                    var64 = 8.7153845
        else:
            if input[1] < 83.0:
                if input[0] < 14.0:
                    var64 = 0.12266083
                else:
                    var64 = 2.6700094
            else:
                if input[2] < 2224.29:
                    var64 = 6.5615244
                else:
                    var64 = 3.662661
    if input[6] < 14.0:
        if input[1] < 112.0:
            if input[6] < 6.0:
                if input[4] < 7.056667:
                    var65 = -0.2524053
                else:
                    var65 = -2.1033719
            else:
                if input[8] < 72.0:
                    var65 = -0.3538828
                else:
                    var65 = 1.3681
        else:
            if input[0] < 12.0:
                if input[4] < 234.04666:
                    var65 = 1.5445188
                else:
                    var65 = -0.762554
            else:
                if input[1] < 301.0:
                    var65 = 1.171214
                else:
                    var65 = 4.7757487
    else:
        if input[1] < 104.0:
            if input[4] < 562.6275:
                if input[6] < 22.0:
                    var65 = 0.03196447
                else:
                    var65 = 2.2937489
            else:
                if input[4] < 582.37:
                    var65 = -16.57134
                else:
                    var65 = 1.2221859
        else:
            if input[0] < 4.0:
                if input[7] < 44.0:
                    var65 = 1.7980789
                else:
                    var65 = 6.2027407
            else:
                if input[8] < 99.0:
                    var65 = 4.099506
                else:
                    var65 = -2.6157625
    if input[1] < 872.0:
        if input[2] < 1249.41:
            if input[4] < 241.62714:
                if input[2] < 268.91:
                    var66 = 0.14744174
                else:
                    var66 = 2.019323
            else:
                if input[4] < 245.9425:
                    var66 = -18.135288
                else:
                    var66 = -0.11030181
        else:
            if input[0] < 12.0:
                if input[0] < 8.0:
                    var66 = 3.2425199
                else:
                    var66 = 1.2318308
            else:
                if input[1] < 725.0:
                    var66 = 5.5120807
                else:
                    var66 = 1.9366598
    else:
        if input[3] < 188.4:
            if input[2] < 1807.71:
                if input[2] < 865.92:
                    var66 = 3.5318773
                else:
                    var66 = 6.8547387
            else:
                if input[1] < 1096.0:
                    var66 = 1.4410659
                else:
                    var66 = 4.484044
        else:
            if input[2] < 1815.6:
                if input[2] < 1742.62:
                    var66 = 2.1803272
                else:
                    var66 = -17.095823
            else:
                if input[2] < 2424.47:
                    var66 = 4.72962
                else:
                    var66 = 0.61750793
    if input[2] < 1171.99:
        if input[1] < 836.0:
            if input[8] < 99.0:
                if input[2] < 311.43:
                    var67 = -0.21274638
                else:
                    var67 = 1.4572941
            else:
                if input[2] < 631.88:
                    var67 = -1.5039192
                else:
                    var67 = -5.0091853
        else:
            if input[3] < 188.4:
                if input[2] < 1013.03:
                    var67 = 3.3941498
                else:
                    var67 = 8.01886
            else:
                if input[3] < 199.66667:
                    var67 = -1.3927109
                else:
                    var67 = 1.7238749
    else:
        if input[9] < 67.0:
            if input[4] < 153.15:
                if input[8] < 45.0:
                    var67 = 5.909412
                else:
                    var67 = 4.0061755
            else:
                if input[2] < 1411.49:
                    var67 = 1.3774623
                else:
                    var67 = 3.4080951
        else:
            if input[1] < 1004.0:
                if input[1] < 483.0:
                    var67 = -1.2374023
                else:
                    var67 = 3.0954092
            else:
                var67 = -16.668428
    if input[0] < 13.0:
        if input[1] < 213.0:
            if input[1] < 195.73:
                if input[1] < 94.0:
                    var68 = -0.3660576
                else:
                    var68 = 1.8279499
            else:
                if input[1] < 198.0:
                    var68 = -11.838552
                else:
                    var68 = 0.19554977
        else:
            if input[0] < 2.0:
                if input[1] < 1086.0:
                    var68 = -0.10508149
                else:
                    var68 = 5.0327945
            else:
                if input[2] < 1143.58:
                    var68 = 1.8497279
                else:
                    var68 = 3.0119853
    else:
        if input[8] < 99.0:
            if input[2] < 486.02:
                if input[1] < 301.0:
                    var68 = -1.0098804
                else:
                    var68 = 3.0998769
            else:
                if input[2] < 2224.29:
                    var68 = 5.694681
                else:
                    var68 = 2.689085
        else:
            var68 = -3.6079545
    if input[0] < 13.0:
        if input[1] < 1100.0:
            if input[7] < 43.0:
                if input[2] < 1084.16:
                    var69 = 0.9111461
                else:
                    var69 = 2.3404906
            else:
                if input[1] < 1086.0:
                    var69 = -16.24909
                else:
                    var69 = 0.6482987
        else:
            if input[3] < 115.75:
                if input[0] < 12.0:
                    var69 = 7.6080565
                else:
                    var69 = 2.1419902
            else:
                if input[8] < 25.0:
                    var69 = 6.3374186
                else:
                    var69 = 2.9233522
    else:
        if input[1] < 69.0:
            if input[2] < 124.65:
                var69 = -1.640274
            else:
                if input[1] < 14.0:
                    var69 = -0.23724365
                else:
                    var69 = 1.2202033
        else:
            if input[8] < 30.0:
                if input[2] < 431.95:
                    var69 = 0.082545474
                else:
                    var69 = 6.6677337
            else:
                if input[8] < 70.0:
                    var69 = 2.4217565
                else:
                    var69 = 5.528688
    if input[0] < 10.0:
        if input[1] < 753.0:
            if input[8] < 50.0:
                if input[8] < 49.0:
                    var70 = 1.3994318
                else:
                    var70 = -13.938247
            else:
                if input[4] < 190.612:
                    var70 = 0.45317227
                else:
                    var70 = 2.4784973
        else:
            if input[7] < 4.0:
                if input[2] < 47.46:
                    var70 = 3.43127
                else:
                    var70 = -2.1963756
            else:
                if input[7] < 14.0:
                    var70 = 3.21116
                else:
                    var70 = 1.0997511
    else:
        if input[1] < 1025.03:
            if input[0] < 14.0:
                if input[2] < 214.08:
                    var70 = -1.9513397
                else:
                    var70 = 2.4394083
            else:
                if input[1] < 770.0:
                    var70 = 5.428831
                else:
                    var70 = 2.004767
        else:
            if input[8] < 44.0:
                if input[2] < 1990.0:
                    var70 = 8.9751005
                else:
                    var70 = 1.3025391
            else:
                if input[2] < 347.82:
                    var70 = 0.38497752
                else:
                    var70 = 5.2828984
    var71 = var15 + var16 + var17 + var18 + var19 + var20 + var21 + var22 + var23 + var24 + var25 + var26 + var27 + var28 + var29 + var30 + var31 + var32 + var33 + var34 + var35 + var36 + var37 + var38 + var39 + var40 + var41 + var42 + var43 + var44 + var45 + var46 + var47 + var48 + var49 + var50 + var51 + var52 + var53 + var54 + var55 + var56 + var57 + var58 + var59 + var60 + var61 + var62 + var63 + var64 + var65 + var66 + var67 + var68 + var69 + var70
    if input[1] < 1086.0:
        if input[7] < 43.0:
            if input[2] < 1241.21:
                if input[0] < 13.0:
                    var72 = 0.87161964
                else:
                    var72 = 3.9019105
            else:
                if input[8] < 48.0:
                    var72 = 3.2501245
                else:
                    var72 = 1.743939
        else:
            var72 = -15.870354
    else:
        if input[3] < 143.0:
            if input[3] < 78.75:
                if input[1] < 1096.0:
                    var72 = 0.4982941
                else:
                    var72 = -0.6621796
            else:
                if input[1] < 1185.0:
                    var72 = 6.5574656
                else:
                    var72 = 2.6605053
        else:
            if input[3] < 148.125:
                if input[2] < 106.86:
                    var72 = 0.1083313
                else:
                    var72 = -2.8854473
            else:
                if input[1] < 1175.0:
                    var72 = 2.3888597
                else:
                    var72 = 5.4908314
    if input[0] < 10.0:
        if input[1] < 756.0:
            if input[2] < 1448.55:
                if input[2] < 1411.49:
                    var73 = 0.49841142
                else:
                    var73 = -9.927518
            else:
                if input[0] < 3.0:
                    var73 = -0.09885728
                else:
                    var73 = 2.5618038
        else:
            if input[7] < 4.0:
                if input[3] < 95.4:
                    var73 = 1.2125194
                else:
                    var73 = -4.844122
            else:
                if input[2] < 999.45:
                    var73 = 1.4030981
                else:
                    var73 = 2.889142
    else:
        if input[1] < 1020.0:
            if input[0] < 14.0:
                if input[2] < 202.49:
                    var73 = -1.0778376
                else:
                    var73 = 2.320719
            else:
                if input[8] < 98.0:
                    var73 = 4.4190288
                else:
                    var73 = -3.889238
        else:
            if input[8] < 44.0:
                if input[1] < 1025.03:
                    var73 = -0.70719606
                else:
                    var73 = 7.513523
            else:
                if input[8] < 70.0:
                    var73 = 0.67309797
                else:
                    var73 = 5.6264954
    if input[5] < 12.0:
        if input[2] < 1246.48:
            if input[2] < 1227.21:
                if input[8] < 99.0:
                    var74 = 0.48455715
                else:
                    var74 = -3.079658
            else:
                if input[1] < 198.0:
                    var74 = -17.164686
                else:
                    var74 = 1.8347565
        else:
            if input[4] < 153.15:
                if input[2] < 1712.85:
                    var74 = 3.8246064
                else:
                    var74 = 8.035775
            else:
                if input[1] < 477.0:
                    var74 = 1.9274262
                else:
                    var74 = -1.4418386
    else:
        if input[1] < 1100.0:
            if input[7] < 43.0:
                if input[2] < 709.07:
                    var74 = 0.9030062
                else:
                    var74 = 2.4478686
            else:
                if input[1] < 1086.0:
                    var74 = -15.545824
                else:
                    var74 = 0.5097992
        else:
            if input[8] < 44.0:
                if input[0] < 9.0:
                    var74 = 2.1273782
                else:
                    var74 = 7.278141
            else:
                if input[0] < 12.0:
                    var74 = 3.6644552
                else:
                    var74 = -0.32576752
    if input[0] < 10.0:
        if input[8] < 47.0:
            if input[2] < 290.78:
                if input[0] < 5.0:
                    var75 = 0.52207077
                else:
                    var75 = -1.8488064
            else:
                if input[1] < 934.0:
                    var75 = 1.9640675
                else:
                    var75 = 4.0048823
        else:
            if input[8] < 50.0:
                if input[2] < 579.29:
                    var75 = -1.9810333
                else:
                    var75 = -17.012259
            else:
                if input[8] < 99.0:
                    var75 = 1.4697493
                else:
                    var75 = -2.533833
    else:
        if input[3] < 97.6:
            if input[0] < 13.0:
                if input[2] < 1179.9:
                    var75 = 1.0813829
                else:
                    var75 = 2.3379216
            else:
                if input[1] < 83.0:
                    var75 = 1.2680308
                else:
                    var75 = 3.9688504
        else:
            if input[1] < 1192.0:
                var75 = 6.5974116
            else:
                var75 = -0.54358214
    if input[2] < 716.7:
        if input[0] < 12.0:
            if input[4] < 140.93857:
                if input[2] < 311.43:
                    var76 = -0.15366626
                else:
                    var76 = 1.5607221
            else:
                if input[0] < 5.0:
                    var76 = -0.5128833
                else:
                    var76 = -6.09242
        else:
            if input[2] < 517.54:
                if input[8] < 94.0:
                    var76 = 1.21491
                else:
                    var76 = 7.051098
            else:
                if input[2] < 587.38:
                    var76 = 8.25222
                else:
                    var76 = 1.4976143
    else:
        if input[8] < 99.0:
            if input[5] < 2.0:
                if input[1] < 69.0:
                    var76 = 1.136851
                else:
                    var76 = -3.1229036
            else:
                if input[9] < 27.0:
                    var76 = 2.5467598
                else:
                    var76 = 0.77098775
        else:
            var76 = -5.2842255
    if input[0] < 11.0:
        if input[1] < 72.0:
            if input[1] < 66.13:
                if input[2] < 1059.79:
                    var77 = -1.5247767
                else:
                    var77 = 1.0823919
            else:
                if input[0] < 4.0:
                    var77 = 0.02501068
                else:
                    var77 = -15.676679
        else:
            if input[0] < 2.0:
                if input[1] < 534.0:
                    var77 = -1.5096049
                else:
                    var77 = 0.83935004
            else:
                if input[2] < 407.43:
                    var77 = 0.28553838
                else:
                    var77 = 1.6431378
    else:
        if input[1] < 1014.0:
            if input[0] < 14.0:
                if input[2] < 214.08:
                    var77 = -1.2892456
                else:
                    var77 = 1.9367307
            else:
                if input[8] < 96.0:
                    var77 = 4.1892104
                else:
                    var77 = -0.8986975
        else:
            if input[2] < 2253.61:
                if input[8] < 37.0:
                    var77 = 6.5045457
                else:
                    var77 = 3.850261
            else:
                if input[4] < 190.612:
                    var77 = 1.2167984
                else:
                    var77 = -0.35982868
    if input[1] < 313.0:
        if input[8] < 32.0:
            if input[1] < 17.0:
                if input[0] < 5.0:
                    var78 = 0.19104868
                else:
                    var78 = -1.813115
            else:
                if input[0] < 3.0:
                    var78 = 0.03337091
                else:
                    var78 = 1.889223
        else:
            if input[8] < 50.0:
                if input[8] < 48.0:
                    var78 = 0.5677652
                else:
                    var78 = -13.353354
            else:
                if input[2] < 517.54:
                    var78 = -0.7334067
                else:
                    var78 = 1.7063067
    else:
        if input[3] < 356.5:
            if input[8] < 99.0:
                if input[2] < 347.82:
                    var78 = 0.75238603
                else:
                    var78 = 2.4659328
            else:
                if input[0] < 9.0:
                    var78 = -4.2901998
                else:
                    var78 = -0.14907913
        else:
            if input[1] < 1162.0:
                if input[7] < 43.0:
                    var78 = 0.14867647
                else:
                    var78 = -3.731929
            else:
                if input[0] < 3.0:
                    var78 = 5.631781
                else:
                    var78 = -0.74761355
    if input[1] < 313.0:
        if input[0] < 14.0:
            if input[3] < 67.36364:
                if input[3] < 46.6:
                    var79 = 0.1796522
                else:
                    var79 = 2.1187437
            else:
                if input[3] < 72.666664:
                    var79 = -9.424137
                else:
                    var79 = -0.1699351
        else:
            if input[1] < 83.0:
                if input[2] < 449.83:
                    var79 = -0.10912323
                else:
                    var79 = 1.4765946
            else:
                var79 = 4.5193563
    else:
        if input[7] < 14.0:
            if input[2] < 214.08:
                if input[4] < 8.236:
                    var79 = 2.8159404
                else:
                    var79 = -0.68406266
            else:
                if input[1] < 993.0:
                    var79 = 1.7726687
                else:
                    var79 = 2.9801154
        else:
            if input[7] < 44.0:
                if input[7] < 43.0:
                    var79 = 0.29591888
                else:
                    var79 = -9.422259
            else:
                if input[2] < 863.93:
                    var79 = -0.39634705
                else:
                    var79 = 4.9801393
    if input[1] < 89.0:
        if input[2] < 2317.31:
            if input[2] < 1227.21:
                if input[2] < 364.79:
                    var80 = -1.2550018
                else:
                    var80 = 0.05263966
            else:
                if input[3] < 8.857142:
                    var80 = 2.1987846
                else:
                    var80 = 0.029178292
        else:
            if input[0] < 5.0:
                var80 = -14.955419
            else:
                if input[0] < 8.0:
                    var80 = -1.0013062
                else:
                    var80 = 0.08157959
    else:
        if input[0] < 11.0:
            if input[8] < 46.0:
                if input[2] < 1164.37:
                    var80 = 1.1476231
                else:
                    var80 = 2.6841733
            else:
                if input[8] < 50.0:
                    var80 = -4.9351263
                else:
                    var80 = 1.3777077
        else:
            if input[8] < 99.0:
                if input[2] < 2317.31:
                    var80 = 2.8083289
                else:
                    var80 = 0.34546813
            else:
                if input[0] < 12.0:
                    var80 = -0.65591943
                else:
                    var80 = -3.7002518
    if input[2] < 1129.52:
        if input[8] < 99.0:
            if input[1] < 94.0:
                if input[8] < 28.0:
                    var81 = 0.706618
                else:
                    var81 = -1.1528003
            else:
                if input[0] < 11.0:
                    var81 = 0.6911396
                else:
                    var81 = 2.1053588
        else:
            if input[2] < 631.88:
                if input[0] < 7.0:
                    var81 = -2.3013008
                else:
                    var81 = -0.23620681
            else:
                var81 = -4.825222
    else:
        if input[1] < 1182.0:
            if input[4] < 153.15:
                if input[4] < 143.48625:
                    var81 = 2.419668
                else:
                    var81 = 5.0729055
            else:
                if input[0] < 8.0:
                    var81 = 1.7550992
                else:
                    var81 = 0.44139966
        else:
            if input[0] < 13.0:
                if input[4] < 317.99167:
                    var81 = 7.0589385
                else:
                    var81 = 3.4481971
            else:
                var81 = 0.5346924
    if input[8] < 99.0:
        if input[2] < 407.43:
            if input[1] < 85.0:
                if input[0] < 9.0:
                    var82 = -2.077531
                else:
                    var82 = -0.30351818
            else:
                if input[3] < 7.5:
                    var82 = 6.0745287
                else:
                    var82 = 0.3532316
        else:
            if input[0] < 13.0:
                if input[1] < 1185.0:
                    var82 = 1.2013242
                else:
                    var82 = 5.598879
            else:
                if input[8] < 30.0:
                    var82 = 4.191424
                else:
                    var82 = 2.0408323
    else:
        if input[2] < 631.88:
            if input[3] < 66.666664:
                if input[0] < 10.0:
                    var82 = 0.68102723
                else:
                    var82 = -0.17811279
            else:
                if input[3] < 183.8:
                    var82 = -2.4283369
                else:
                    var82 = -0.54034805
        else:
            var82 = -4.704683
    if input[1] < 94.0:
        if input[4] < 554.7167:
            if input[0] < 11.0:
                if input[0] < 3.0:
                    var83 = -1.781881
                else:
                    var83 = -0.56551766
            else:
                if input[8] < 28.0:
                    var83 = 2.285179
                else:
                    var83 = -0.20326963
        else:
            if input[0] < 3.0:
                if input[0] < 2.0:
                    var83 = -0.14003967
                else:
                    var83 = 2.3078554
            else:
                var83 = -14.655443
    else:
        if input[8] < 99.0:
            if input[1] < 1100.0:
                if input[0] < 13.0:
                    var83 = 1.1506937
                else:
                    var83 = 2.9009135
            else:
                if input[4] < 208.32:
                    var83 = 3.553351
                else:
                    var83 = 1.7963008
        else:
            if input[3] < 34.6:
                if input[1] < 173.0:
                    var83 = -0.739682
                else:
                    var83 = -5.056767
            else:
                if input[3] < 67.36364:
                    var83 = 0.039946746
                else:
                    var83 = -1.6348326
    if input[8] < 99.0:
        if input[1] < 94.0:
            if input[4] < 562.6275:
                if input[1] < 17.0:
                    var84 = -1.5356733
                else:
                    var84 = 0.28709626
            else:
                if input[0] < 3.0:
                    var84 = 0.88933164
                else:
                    var84 = -14.289057
        else:
            if input[0] < 4.0:
                if input[9] < 71.0:
                    var84 = 0.54277796
                else:
                    var84 = -1.7421893
            else:
                if input[4] < 316.74667:
                    var84 = 1.3803905
                else:
                    var84 = 3.0581129
    else:
        if input[2] < 631.88:
            if input[7] < 3.0:
                if input[0] < 4.0:
                    var84 = 0.56249315
                else:
                    var84 = -0.43555054
            else:
                if input[4] < 258.2443:
                    var84 = -2.524248
                else:
                    var84 = -0.4859688
        else:
            if input[0] < 5.0:
                var84 = -1.3096802
            else:
                var84 = -4.7530794
    if input[2] < 540.6:
        if input[1] < 85.0:
            if input[4] < 39.6625:
                if input[0] < 9.0:
                    var85 = -1.7973309
                else:
                    var85 = -0.15949586
            else:
                if input[0] < 5.0:
                    var85 = -0.37914276
                else:
                    var85 = 1.062384
        else:
            if input[3] < 7.5:
                var85 = 5.815633
            else:
                if input[8] < 4.0:
                    var85 = 2.6407008
                else:
                    var85 = 0.2267257
    else:
        if input[1] < 989.0:
            if input[0] < 3.0:
                if input[1] < 508.0:
                    var85 = -1.3381809
                else:
                    var85 = 0.8190867
            else:
                if input[8] < 99.0:
                    var85 = 1.4578283
                else:
                    var85 = -3.5001264
        else:
            if input[4] < 169.41692:
                if input[2] < 1349.61:
                    var85 = 5.268926
                else:
                    var85 = 0.8214245
            else:
                if input[4] < 1300.17:
                    var85 = 1.2189176
                else:
                    var85 = 5.1609874
    if input[1] < 1100.0:
        if input[7] < 43.0:
            if input[2] < 1422.11:
                if input[0] < 10.0:
                    var86 = 0.21113992
                else:
                    var86 = 1.3144006
            else:
                if input[0] < 8.0:
                    var86 = 2.2259305
                else:
                    var86 = 0.76216745
        else:
            if input[1] < 1086.0:
                var86 = -14.508049
            else:
                var86 = 0.6724457
    else:
        if input[3] < 115.75:
            if input[0] < 14.0:
                if input[2] < 2253.61:
                    var86 = 4.581826
                else:
                    var86 = 0.26272583
            else:
                var86 = -1.2341553
        else:
            if input[3] < 577.5:
                if input[3] < 381.0:
                    var86 = 2.0426462
                else:
                    var86 = -1.5903443
            else:
                if input[2] < 927.74:
                    var86 = 1.777034
                else:
                    var86 = 4.768638
    if input[0] < 13.0:
        if input[1] < 697.0:
            if input[8] < 48.0:
                if input[0] < 2.0:
                    var87 = -1.1222514
                else:
                    var87 = 1.0816802
            else:
                if input[8] < 50.0:
                    var87 = -10.511291
                else:
                    var87 = 0.6195806
        else:
            if input[8] < 99.0:
                if input[1] < 1175.0:
                    var87 = 1.3029133
                else:
                    var87 = 3.9847066
            else:
                if input[0] < 9.0:
                    var87 = -3.7594934
                else:
                    var87 = -0.36564636
    else:
        if input[8] < 96.0:
            if input[8] < 78.0:
                if input[8] < 30.0:
                    var87 = 4.210682
                else:
                    var87 = 1.8719962
            else:
                if input[1] < 633.0:
                    var87 = 6.8013763
                else:
                    var87 = 2.9523103
        else:
            if input[8] < 99.0:
                if input[1] < 69.0:
                    var87 = -0.55059713
                else:
                    var87 = 0.35908204
            else:
                var87 = -3.0696092
    if input[1] < 313.0:
        if input[8] < 17.0:
            if input[1] < 32.0:
                if input[8] < 2.0:
                    var88 = 0.35968477
                else:
                    var88 = -1.372086
            else:
                if input[1] < 301.0:
                    var88 = 1.7566761
                else:
                    var88 = -1.7907288
        else:
            if input[8] < 50.0:
                if input[8] < 48.0:
                    var88 = 0.17553183
                else:
                    var88 = -15.596702
            else:
                if input[2] < 555.49:
                    var88 = -0.52213037
                else:
                    var88 = 0.9539483
    else:
        if input[7] < 14.0:
            if input[2] < 347.82:
                if input[8] < 20.0:
                    var88 = -1.6146307
                else:
                    var88 = 0.6024444
            else:
                if input[8] < 99.0:
                    var88 = 1.6994467
                else:
                    var88 = -1.738707
        else:
            if input[7] < 19.0:
                if input[2] < 202.49:
                    var88 = 1.4775696
                else:
                    var88 = -1.8176543
            else:
                if input[1] < 1086.0:
                    var88 = -0.039673537
                else:
                    var88 = 3.876269
    if input[1] < 1175.0:
        if input[8] < 49.0:
            if input[2] < 967.0:
                if input[8] < 48.0:
                    var89 = 0.19649245
                else:
                    var89 = 4.2558846
            else:
                if input[1] < 999.0:
                    var89 = 1.2124599
                else:
                    var89 = 2.9641185
        else:
            if input[8] < 50.0:
                if input[2] < 716.7:
                    var89 = -2.445858
                else:
                    var89 = -25.49111
            else:
                if input[8] < 99.0:
                    var89 = 0.79766315
                else:
                    var89 = -2.629205
    else:
        if input[2] < 1901.83:
            if input[4] < 1.9266666:
                var89 = 0.20968628
            else:
                if input[8] < 8.0:
                    var89 = 2.7600923
                else:
                    var89 = 6.149063
        else:
            if input[8] < 14.0:
                var89 = 3.1468894
            else:
                if input[0] < 5.0:
                    var89 = -0.7638489
                else:
                    var89 = 0.53458256
    if input[1] < 94.0:
        if input[2] < 2462.26:
            if input[2] < 2248.68:
                if input[2] < 364.79:
                    var90 = -1.3369273
                else:
                    var90 = 0.007278755
            else:
                if input[0] < 5.0:
                    var90 = -12.733948
                else:
                    var90 = -0.81813204
        else:
            if input[0] < 5.0:
                var90 = 3.1266623
            else:
                var90 = 0.20840454
    else:
        if input[0] < 4.0:
            if input[4] < 1927.75:
                if input[9] < 72.0:
                    var90 = 0.121378206
                else:
                    var90 = -13.539652
            else:
                if input[1] < 828.0:
                    var90 = 0.045168053
                else:
                    var90 = 4.7914233
        else:
            if input[4] < 386.97333:
                if input[4] < 375.698:
                    var90 = 1.0711344
                else:
                    var90 = -6.15743
            else:
                if input[1] < 1012.0:
                    var90 = 3.6372933
                else:
                    var90 = 0.79319394
    if input[0] < 11.0:
        if input[8] < 99.0:
            if input[1] < 753.0:
                if input[2] < 1880.69:
                    var91 = -0.024173308
                else:
                    var91 = 1.2139057
            else:
                if input[2] < 540.6:
                    var91 = 0.02597936
                else:
                    var91 = 1.3331451
        else:
            if input[4] < 79.99:
                if input[0] < 7.0:
                    var91 = -1.2475545
                else:
                    var91 = 0.58304447
            else:
                if input[0] < 5.0:
                    var91 = -0.96991473
                else:
                    var91 = -5.2176447
    else:
        if input[1] < 1020.0:
            if input[1] < 770.0:
                if input[4] < 188.31:
                    var91 = 1.9031705
                else:
                    var91 = -0.40590212
            else:
                if input[1] < 810.0:
                    var91 = -2.8243966
                else:
                    var91 = 0.5391828
        else:
            if input[2] < 1768.53:
                if input[8] < 37.0:
                    var91 = 5.636995
                else:
                    var91 = 2.0375001
            else:
                if input[0] < 12.0:
                    var91 = 4.6908693
                else:
                    var91 = -0.8836589
    if input[0] < 12.0:
        if input[1] < 213.0:
            if input[1] < 195.73:
                if input[1] < 117.0:
                    var92 = -0.7688713
                else:
                    var92 = 0.74540156
            else:
                if input[0] < 5.0:
                    var92 = 1.3547668
                else:
                    var92 = -6.506472
        else:
            if input[8] < 4.0:
                if input[0] < 10.0:
                    var92 = 3.5425916
                else:
                    var92 = -0.07466431
            else:
                if input[7] < 43.0:
                    var92 = 0.6188014
                else:
                    var92 = -3.678555
    else:
        if input[6] < 46.0:
            if input[6] < 24.0:
                if input[4] < 8.236:
                    var92 = 3.6384625
                else:
                    var92 = 0.60369647
            else:
                if input[3] < 73.55556:
                    var92 = 3.1347246
                else:
                    var92 = 0.5618725
        else:
            if input[1] < 403.0:
                if input[1] < 250.0:
                    var92 = 0.26785278
                else:
                    var92 = 2.8840578
            else:
                if input[3] < 58.153847:
                    var92 = -1.6395935
                else:
                    var92 = -0.5271851
    if input[0] < 2.0:
        if input[1] < 1086.0:
            if input[1] < 1062.0:
                if input[1] < 534.0:
                    var93 = -1.4592384
                else:
                    var93 = 0.36856258
            else:
                var93 = -13.142525
        else:
            if input[2] < 863.93:
                if input[1] < 1096.0:
                    var93 = 0.5944916
                else:
                    var93 = -0.6953766
            else:
                var93 = 2.4310882
    else:
        if input[1] < 104.0:
            if input[4] < 562.6275:
                if input[4] < 39.6625:
                    var93 = -1.3290005
                else:
                    var93 = 0.031174151
            else:
                if input[2] < 2328.11:
                    var93 = -12.426726
                else:
                    var93 = 3.0076072
        else:
            if input[8] < 7.0:
                if input[0] < 8.0:
                    var93 = 3.1352818
                else:
                    var93 = 1.0082783
            else:
                if input[8] < 99.0:
                    var93 = 0.87414616
                else:
                    var93 = -1.5688782
    if input[0] < 12.0:
        if input[3] < 39.642:
            if input[3] < 38.95:
                if input[1] < 72.0:
                    var94 = -1.3570703
                else:
                    var94 = 0.10309106
            else:
                if input[4] < 207.11166:
                    var94 = 0.233041
                else:
                    var94 = -9.526089
        else:
            if input[0] < 4.0:
                if input[7] < 19.0:
                    var94 = -0.43623558
                else:
                    var94 = 0.60355055
            else:
                if input[0] < 8.0:
                    var94 = 1.4398464
                else:
                    var94 = 0.2482655
    else:
        if input[2] < 2243.12:
            if input[2] < 1129.52:
                if input[4] < 71.902:
                    var94 = 1.5252122
                else:
                    var94 = -0.47827217
            else:
                if input[4] < 86.75:
                    var94 = 6.488973
                else:
                    var94 = 2.2523744
        else:
            if input[1] < 403.0:
                if input[2] < 2353.5:
                    var94 = 0.67001194
                else:
                    var94 = 2.2234573
            else:
                if input[0] < 14.0:
                    var94 = -1.7578375
                else:
                    var94 = -0.020269012
    if input[1] < 1100.0:
        if input[3] < 1068.0:
            if input[8] < 99.0:
                if input[1] < 94.0:
                    var95 = -0.510941
                else:
                    var95 = 0.72279036
            else:
                if input[2] < 631.88:
                    var95 = -1.31453
                else:
                    var95 = -3.7802892
        else:
            if input[1] < 1070.0:
                var95 = 3.017163
            else:
                var95 = -12.829051
    else:
        if input[8] < 26.0:
            if input[0] < 9.0:
                if input[0] < 8.0:
                    var95 = 2.6982048
                else:
                    var95 = -2.5452697
            else:
                var95 = 5.290869
        else:
            if input[0] < 3.0:
                if input[2] < 2013.45:
                    var95 = 4.9463296
                else:
                    var95 = 0.82615966
            else:
                if input[4] < 208.32:
                    var95 = 2.0186453
                else:
                    var95 = -0.20579319
    if input[5] < 20.0:
        if input[0] < 14.0:
            if input[2] < 1422.11:
                if input[2] < 1411.49:
                    var96 = -0.008960909
                else:
                    var96 = -3.467917
            else:
                if input[2] < 1477.23:
                    var96 = 3.706044
                else:
                    var96 = 0.621406
        else:
            if input[1] < 597.0:
                if input[1] < 83.0:
                    var96 = 0.39275882
                else:
                    var96 = 3.9489095
            else:
                if input[2] < 1129.52:
                    var96 = 1.1824988
                else:
                    var96 = -0.34510836
    else:
        if input[3] < 206.25:
            if input[2] < 1901.83:
                if input[4] < 66.75667:
                    var96 = 1.2068847
                else:
                    var96 = 3.434806
            else:
                if input[3] < 155.57143:
                    var96 = -0.18959628
                else:
                    var96 = 2.3063147
        else:
            if input[4] < 1927.75:
                if input[4] < 1697.08:
                    var96 = 0.33981827
                else:
                    var96 = -12.508326
            else:
                var96 = 5.2645617
    if input[1] < 1100.0:
        if input[7] < 43.0:
            if input[1] < 94.0:
                if input[8] < 47.0:
                    var97 = 0.36422923
                else:
                    var97 = -1.0643028
            else:
                if input[8] < 99.0:
                    var97 = 0.67164445
                else:
                    var97 = -2.115395
        else:
            if input[1] < 1086.0:
                var97 = -12.195618
            else:
                var97 = 0.87677
    else:
        if input[3] < 143.0:
            if input[3] < 78.75:
                var97 = -1.5185333
            else:
                if input[2] < 1871.77:
                    var97 = 5.3762946
                else:
                    var97 = 1.9570427
        else:
            if input[0] < 3.0:
                if input[2] < 927.74:
                    var97 = 1.3203156
                else:
                    var97 = 3.824801
            else:
                if input[8] < 45.0:
                    var97 = -2.274618
                else:
                    var97 = 1.1897957
    if input[0] < 10.0:
        if input[8] < 48.0:
            if input[1] < 891.0:
                if input[0] < 8.0:
                    var98 = 0.76074356
                else:
                    var98 = -1.0416868
            else:
                if input[1] < 1038.0:
                    var98 = 3.1018538
                else:
                    var98 = 0.5442158
        else:
            if input[8] < 50.0:
                if input[2] < 1013.03:
                    var98 = -2.0968702
                else:
                    var98 = -20.730434
            else:
                if input[4] < 201.81166:
                    var98 = -0.35282907
                else:
                    var98 = 0.8970057
    else:
        if input[3] < 99.0:
            if input[0] < 14.0:
                if input[4] < 16.933332:
                    var98 = -1.5731428
                else:
                    var98 = 0.8412749
            else:
                if input[2] < 1210.87:
                    var98 = 3.4486377
                else:
                    var98 = 1.109946
        else:
            if input[3] < 107.57143:
                if input[8] < 23.0:
                    var98 = 1.5178243
                else:
                    var98 = 5.4060955
            else:
                if input[1] < 1153.0:
                    var98 = 1.3832866
                else:
                    var98 = -1.2597169
    if input[2] < 1147.89:
        if input[4] < 247.745:
            if input[4] < 231.4943:
                if input[4] < 8.236:
                    var99 = 1.5451796
                else:
                    var99 = 0.093362704
            else:
                if input[1] < 774.0:
                    var99 = 4.0063844
                else:
                    var99 = -0.64944
        else:
            if input[0] < 4.0:
                if input[2] < 1072.44:
                    var99 = -0.15048721
                else:
                    var99 = -3.0835438
            else:
                if input[1] < 289.0:
                    var99 = -11.658321
                else:
                    var99 = -0.8346314
    else:
        if input[0] < 4.0:
            if input[7] < 44.0:
                if input[7] < 43.0:
                    var99 = -0.04072507
                else:
                    var99 = -11.372467
            else:
                var99 = 3.6696937
        else:
            if input[0] < 8.0:
                if input[1] < 72.0:
                    var99 = -2.8731065
                else:
                    var99 = 2.593621
            else:
                if input[4] < 247.745:
                    var99 = 0.7563029
                else:
                    var99 = -3.2402
    if input[8] < 49.0:
        if input[2] < 341.45:
            if input[1] < 872.0:
                if input[1] < 353.0:
                    var100 = 0.11272293
                else:
                    var100 = -2.2616215
            else:
                if input[3] < 115.75:
                    var100 = 2.2779756
                else:
                    var100 = 0.079814844
        else:
            if input[3] < 206.25:
                if input[2] < 2152.66:
                    var100 = 1.5783232
                else:
                    var100 = 0.20363867
            else:
                if input[3] < 577.5:
                    var100 = -0.5568314
                else:
                    var100 = 2.4943817
    else:
        if input[8] < 50.0:
            if input[2] < 716.7:
                if input[2] < 407.43:
                    var100 = 0.82018214
                else:
                    var100 = -7.2313676
            else:
                var100 = -20.456411
        else:
            if input[8] < 99.0:
                if input[2] < 2359.42:
                    var100 = 0.6585992
                else:
                    var100 = -0.7793479
            else:
                if input[2] < 631.88:
                    var100 = -0.7290017
                else:
                    var100 = -3.6351955
    if input[1] < 1100.0:
        if input[0] < 3.0:
            if input[1] < 1062.0:
                if input[1] < 566.0:
                    var101 = -1.1979042
                else:
                    var101 = 0.3145542
            else:
                if input[1] < 1086.0:
                    var101 = -10.576744
                else:
                    var101 = 0.81972355
        else:
            if input[1] < 85.0:
                if input[4] < 562.6275:
                    var101 = -0.21375597
                else:
                    var101 = -10.956787
            else:
                if input[8] < 99.0:
                    var101 = 0.7990648
                else:
                    var101 = -2.0482416
    else:
        if input[8] < 44.0:
            if input[4] < 254.578:
                if input[2] < 1990.0:
                    var101 = 5.447213
                else:
                    var101 = -0.014059449
            else:
                if input[0] < 3.0:
                    var101 = 2.0878003
                else:
                    var101 = -0.82475996
        else:
            if input[1] < 1116.0:
                if input[2] < 545.84:
                    var101 = 1.6076853
                else:
                    var101 = 5.2268767
            else:
                if input[8] < 67.0:
                    var101 = -0.6853941
                else:
                    var101 = 1.5646476
    if input[8] < 49.0:
        if input[2] < 1129.52:
            if input[2] < 1094.06:
                if input[1] < 955.0:
                    var102 = 0.11278709
                else:
                    var102 = 1.2896402
            else:
                if input[0] < 11.0:
                    var102 = -3.2551782
                else:
                    var102 = -0.48076174
        else:
            if input[9] < 7.0:
                if input[3] < 126.833336:
                    var102 = 1.8457035
                else:
                    var102 = 7.658502
            else:
                if input[0] < 8.0:
                    var102 = 1.2698687
                else:
                    var102 = -0.78165454
    else:
        if input[8] < 50.0:
            if input[2] < 716.7:
                if input[9] < 4.0:
                    var102 = 1.8829854
                else:
                    var102 = -5.977605
            else:
                var102 = -21.63948
        else:
            if input[8] < 76.0:
                if input[9] < 7.0:
                    var102 = 0.22102736
                else:
                    var102 = 1.3908044
            else:
                if input[8] < 99.0:
                    var102 = 0.1188414
                else:
                    var102 = -2.119826
    if input[0] < 13.0:
        if input[1] < 1175.0:
            if input[2] < 314.81:
                if input[2] < 39.86:
                    var103 = 0.74958104
                else:
                    var103 = -0.9401302
            else:
                if input[1] < 313.0:
                    var103 = -0.19212942
                else:
                    var103 = 0.5216796
        else:
            if input[0] < 5.0:
                if input[4] < 544.2833:
                    var103 = -0.72453105
                else:
                    var103 = 4.0125203
            else:
                if input[4] < 131.048:
                    var103 = 1.956644
                else:
                    var103 = 4.762548
    else:
        if input[2] < 486.02:
            if input[2] < 106.86:
                if input[0] < 14.0:
                    var103 = -0.9709737
                else:
                    var103 = 5.080255
            else:
                if input[2] < 449.83:
                    var103 = -0.737657
                else:
                    var103 = -2.8424194
        else:
            if input[2] < 927.74:
                if input[1] < 459.0:
                    var103 = 1.7123816
                else:
                    var103 = 5.4688525
            else:
                if input[2] < 1054.93:
                    var103 = -0.986615
                else:
                    var103 = 1.6770996
    if input[0] < 2.0:
        if input[1] < 1086.0:
            if input[1] < 1070.0:
                if input[1] < 1038.0:
                    var104 = -0.91112566
                else:
                    var104 = 2.7722998
            else:
                var104 = -9.784381
        else:
            if input[2] < 927.74:
                var104 = 0.9143677
            else:
                var104 = 3.410846
    else:
        if input[1] < 1175.0:
            if input[1] < 1158.0:
                if input[2] < 507.59:
                    var104 = 0.067014486
                else:
                    var104 = 0.7292421
            else:
                if input[0] < 3.0:
                    var104 = 0.6083862
                else:
                    var104 = -1.7298262
        else:
            if input[0] < 5.0:
                if input[4] < 544.2833:
                    var104 = -0.456233
                else:
                    var104 = 3.8787677
            else:
                if input[2] < 1990.0:
                    var104 = 3.5560422
                else:
                    var104 = 0.671579
    if input[1] < 238.0:
        if input[2] < 1241.21:
            if input[2] < 1227.21:
                if input[8] < 84.0:
                    var105 = -0.21071772
                else:
                    var105 = -1.3860464
            else:
                if input[0] < 6.0:
                    var105 = -13.060663
                else:
                    var105 = 1.0114685
        else:
            if input[9] < 23.0:
                if input[2] < 2447.82:
                    var105 = 0.9814194
                else:
                    var105 = -0.64967126
            else:
                if input[2] < 2328.11:
                    var105 = -3.314781
                else:
                    var105 = 1.3873872
    else:
        if input[7] < 12.0:
            if input[2] < 159.26:
                if input[8] < 19.0:
                    var105 = -3.194434
                else:
                    var105 = 0.005893744
            else:
                if input[1] < 1185.0:
                    var105 = 0.71677893
                else:
                    var105 = 3.0438557
        else:
            if input[1] < 483.0:
                if input[1] < 389.0:
                    var105 = -1.1108634
                else:
                    var105 = -2.9400582
            else:
                if input[9] < 14.0:
                    var105 = -1.0770787
                else:
                    var105 = 0.6905419
    if input[2] < 407.43:
        if input[0] < 14.0:
            if input[3] < 21.142857:
                if input[1] < 47.0:
                    var106 = -0.517535
                else:
                    var106 = -2.6445558
            else:
                if input[3] < 31.4:
                    var106 = 1.2983292
                else:
                    var106 = -0.36263427
        else:
            if input[2] < 193.05:
                if input[1] < 384.0:
                    var106 = 4.9316835
                else:
                    var106 = 1.0415772
            else:
                if input[1] < 560.0:
                    var106 = 0.48529968
                else:
                    var106 = -1.9653971
    else:
        if input[8] < 93.0:
            if input[8] < 52.0:
                if input[8] < 49.0:
                    var106 = 0.70087904
                else:
                    var106 = -4.8197207
            else:
                if input[8] < 57.0:
                    var106 = 2.008546
                else:
                    var106 = 0.8159502
        else:
            if input[8] < 99.0:
                if input[1] < 597.0:
                    var106 = -1.012771
                else:
                    var106 = 0.4976031
            else:
                if input[3] < 74.416664:
                    var106 = -0.6975438
                else:
                    var106 = -3.2997162
    if input[2] < 974.73:
        if input[2] < 863.93:
            if input[2] < 725.67:
                if input[4] < 8.236:
                    var107 = 1.1754197
                else:
                    var107 = -0.22709815
            else:
                if input[0] < 2.0:
                    var107 = -0.8008453
                else:
                    var107 = 1.740672
        else:
            if input[4] < 180.32428:
                if input[3] < 82.166664:
                    var107 = -0.98632234
                else:
                    var107 = -3.963308
            else:
                if input[2] < 897.4:
                    var107 = -1.7449626
                else:
                    var107 = 1.2142893
    else:
        if input[4] < 150.28334:
            if input[3] < 79.166664:
                if input[2] < 1179.9:
                    var107 = -0.8887877
                else:
                    var107 = 1.7042803
            else:
                if input[2] < 1013.03:
                    var107 = -1.5854981
                else:
                    var107 = 3.6623666
        else:
            if input[0] < 8.0:
                if input[0] < 4.0:
                    var107 = 0.047827218
                else:
                    var107 = 1.5258402
            else:
                if input[0] < 9.0:
                    var107 = -2.251532
                else:
                    var107 = 0.26956746
    if input[1] < 213.0:
        if input[1] < 195.73:
            if input[5] < 2.0:
                if input[2] < 2462.26:
                    var108 = -0.6780757
                else:
                    var108 = 2.1060333
            else:
                if input[4] < 616.0725:
                    var108 = 0.4814105
                else:
                    var108 = -1.7536938
        else:
            if input[1] < 198.0:
                var108 = -12.651798
            else:
                if input[8] < 84.0:
                    var108 = 1.0161567
                else:
                    var108 = -3.6192346
    else:
        if input[3] < 64.22222:
            if input[3] < 62.0:
                if input[0] < 12.0:
                    var108 = 0.5017387
                else:
                    var108 = 1.8008717
            else:
                if input[8] < 74.0:
                    var108 = 4.3073144
                else:
                    var108 = -0.84757996
        else:
            if input[3] < 72.666664:
                if input[2] < 716.7:
                    var108 = 1.9798596
                else:
                    var108 = -2.2262132
            else:
                if input[2] < 407.43:
                    var108 = -0.44089946
                else:
                    var108 = 0.5710806
    if input[1] < 1175.0:
        if input[9] < 6.0:
            if input[4] < 93.88143:
                if input[3] < 130.2:
                    var109 = 0.30248296
                else:
                    var109 = -1.0927715
            else:
                if input[1] < 1077.0:
                    var109 = 0.9388248
                else:
                    var109 = 4.335046
        else:
            if input[0] < 8.0:
                if input[8] < 50.0:
                    var109 = -0.2039469
                else:
                    var109 = 0.8486415
            else:
                if input[0] < 9.0:
                    var109 = -2.7240758
                else:
                    var109 = 0.06957816
    else:
        if input[4] < 2.850909:
            var109 = -1.2106038
        else:
            if input[3] < 91.666664:
                var109 = -0.16752015
            else:
                if input[8] < 17.0:
                    var109 = 1.3882604
                else:
                    var109 = 3.5484955
    if input[2] < 1422.11:
        if input[2] < 1411.49:
            if input[1] < 955.0:
                if input[4] < 115.82:
                    var110 = 0.20221503
                else:
                    var110 = -0.55604374
            else:
                if input[0] < 7.0:
                    var110 = -0.31865308
                else:
                    var110 = 1.9834503
        else:
            if input[0] < 8.0:
                if input[0] < 5.0:
                    var110 = 2.14852
                else:
                    var110 = 0.007424927
            else:
                var110 = -12.150795
    else:
        if input[8] < 94.0:
            if input[0] < 8.0:
                if input[4] < 254.578:
                    var110 = 4.801428
                else:
                    var110 = 1.0162432
            else:
                if input[4] < 298.855:
                    var110 = 0.51132244
                else:
                    var110 = -4.793402
        else:
            if input[4] < 221.094:
                if input[0] < 12.0:
                    var110 = -3.1803353
                else:
                    var110 = -0.545459
            else:
                if input[8] < 97.0:
                    var110 = -1.3148636
                else:
                    var110 = 0.67194337
    if input[7] < 14.0:
        if input[8] < 99.0:
            if input[1] < 238.0:
                if input[2] < 1241.21:
                    var111 = -0.35453424
                else:
                    var111 = 0.5548253
            else:
                if input[1] < 512.0:
                    var111 = 1.0383751
                else:
                    var111 = 0.25175506
        else:
            if input[4] < 79.99:
                if input[1] < 601.0:
                    var111 = 0.5599266
                else:
                    var111 = -0.8830597
            else:
                if input[4] < 205.92818:
                    var111 = -3.3176258
                else:
                    var111 = -0.7697563
    else:
        if input[7] < 19.0:
            if input[2] < 202.49:
                var111 = 1.4019135
            else:
                if input[8] < 72.0:
                    var111 = -1.9689163
                else:
                    var111 = -0.18029219
        else:
            if input[2] < 1815.6:
                if input[2] < 1707.28:
                    var111 = 0.1858013
                else:
                    var111 = -9.472325
            else:
                if input[7] < 34.0:
                    var111 = 0.75898004
                else:
                    var111 = 4.3307495
    if input[1] < 1100.0:
        if input[2] < 1422.11:
            if input[2] < 1411.49:
                if input[9] < 21.0:
                    var112 = 0.18513854
                else:
                    var112 = -1.3535066
            else:
                if input[0] < 8.0:
                    var112 = 1.3929728
                else:
                    var112 = -11.872985
        else:
            if input[0] < 8.0:
                if input[0] < 4.0:
                    var112 = 0.2854341
                else:
                    var112 = 1.981641
            else:
                if input[9] < 10.0:
                    var112 = 0.35063002
                else:
                    var112 = -3.0299354
    else:
        if input[3] < 143.0:
            if input[9] < 1.0:
                if input[8] < 37.0:
                    var112 = 4.279599
                else:
                    var112 = -1.7008142
            else:
                if input[9] < 8.0:
                    var112 = 3.5498333
                else:
                    var112 = 0.98002404
        else:
            if input[3] < 147.33333:
                var112 = -4.041569
            else:
                if input[1] < 1182.0:
                    var112 = 0.33055514
                else:
                    var112 = 2.37526
    if input[0] < 10.0:
        if input[0] < 8.0:
            if input[0] < 6.0:
                if input[8] < 52.0:
                    var113 = -0.58780414
                else:
                    var113 = 0.37542397
            else:
                if input[2] < 1656.04:
                    var113 = 0.2531732
                else:
                    var113 = 2.0957577
        else:
            if input[2] < 1349.61:
                if input[8] < 29.0:
                    var113 = -1.7222465
                else:
                    var113 = 0.5672614
            else:
                if input[2] < 1422.11:
                    var113 = -6.4300866
                else:
                    var113 = -2.0247204
    else:
        if input[3] < 97.6:
            if input[1] < 798.0:
                if input[3] < 72.85714:
                    var113 = 0.57538897
                else:
                    var113 = 6.2335296
            else:
                if input[1] < 1020.0:
                    var113 = -1.0102993
                else:
                    var113 = 1.0447234
        else:
            if input[1] < 1192.0:
                if input[4] < 205.0089:
                    var113 = 3.6894174
                else:
                    var113 = 0.4501709
            else:
                var113 = -1.4143066
    if input[0] < 14.0:
        if input[1] < 1175.0:
            if input[4] < 16.933332:
                if input[2] < 58.24:
                    var114 = 0.17698127
                else:
                    var114 = -2.3698797
            else:
                if input[4] < 21.13:
                    var114 = 2.3750262
                else:
                    var114 = 0.09174184
        else:
            if input[0] < 5.0:
                if input[0] < 3.0:
                    var114 = 3.5269697
                else:
                    var114 = -0.78216684
            else:
                if input[2] < 1990.0:
                    var114 = 3.5930612
                else:
                    var114 = 0.29663086
    else:
        if input[8] < 96.0:
            if input[1] < 553.0:
                if input[2] < 587.38:
                    var114 = 4.5699105
                else:
                    var114 = 2.5094888
            else:
                if input[2] < 517.54:
                    var114 = -1.045918
                else:
                    var114 = 1.2932752
        else:
            if input[1] < 83.0:
                if input[1] < 69.0:
                    var114 = -0.21824189
                else:
                    var114 = 0.09664001
            else:
                var114 = -2.8768678
    if input[8] < 99.0:
        if input[7] < 42.0:
            if input[9] < 6.0:
                if input[2] < 1191.4:
                    var115 = 0.29700515
                else:
                    var115 = 1.7963098
            else:
                if input[0] < 8.0:
                    var115 = 0.3451427
                else:
                    var115 = -0.7172188
        else:
            if input[2] < 1607.8:
                var115 = 1.7735602
            else:
                var115 = 4.3058944
    else:
        if input[2] < 631.88:
            if input[7] < 3.0:
                if input[0] < 10.0:
                    var115 = 0.9578125
                else:
                    var115 = -0.19984232
            else:
                if input[0] < 2.0:
                    var115 = -0.5186672
                else:
                    var115 = -1.9975363
        else:
            if input[0] < 5.0:
                var115 = -0.6300934
            else:
                var115 = -4.552541
    if input[0] < 13.0:
        if input[8] < 10.0:
            if input[0] < 8.0:
                if input[0] < 5.0:
                    var116 = 0.26658112
                else:
                    var116 = 2.9930618
            else:
                if input[8] < 8.0:
                    var116 = -0.80352
                else:
                    var116 = 2.5268686
        else:
            if input[8] < 52.0:
                if input[8] < 49.0:
                    var116 = 0.16528451
                else:
                    var116 = -3.9707074
            else:
                if input[8] < 76.0:
                    var116 = 0.7890034
                else:
                    var116 = -0.04219126
    else:
        if input[8] < 95.0:
            if input[2] < 2224.29:
                if input[2] < 517.54:
                    var116 = 0.21409968
                else:
                    var116 = 2.092217
            else:
                if input[1] < 195.73:
                    var116 = 2.3520916
                else:
                    var116 = -1.2488304
        else:
            if input[8] < 99.0:
                if input[0] < 14.0:
                    var116 = -0.80069274
                else:
                    var116 = -0.116629794
            else:
                var116 = -2.6911316
    if input[1] < 313.0:
        if input[8] < 32.0:
            if input[1] < 19.0:
                if input[0] < 5.0:
                    var117 = 0.07642784
                else:
                    var117 = -1.8775177
            else:
                if input[0] < 3.0:
                    var117 = -0.36410207
                else:
                    var117 = 0.9405431
        else:
            if input[8] < 50.0:
                if input[8] < 48.0:
                    var117 = -0.45265302
                else:
                    var117 = -8.754111
            else:
                if input[4] < 121.096664:
                    var117 = -0.5303121
                else:
                    var117 = 0.4877204
    else:
        if input[7] < 14.0:
            if input[1] < 512.0:
                if input[1] < 483.0:
                    var117 = 0.6889046
                else:
                    var117 = 3.1831908
            else:
                if input[7] < 4.0:
                    var117 = -0.21271408
                else:
                    var117 = 0.7708947
        else:
            if input[7] < 21.0:
                if input[2] < 202.49:
                    var117 = 1.3630829
                else:
                    var117 = -1.4835483
            else:
                if input[1] < 1086.0:
                    var117 = -0.115889505
                else:
                    var117 = 2.314737
    if input[0] < 11.0:
        if input[1] < 72.0:
            if input[1] < 69.0:
                if input[4] < 263.01334:
                    var118 = -1.3923687
                else:
                    var118 = 0.0034049295
            else:
                var118 = -9.734965
        else:
            if input[2] < 1338.65:
                if input[2] < 1227.21:
                    var118 = -0.084556594
                else:
                    var118 = -1.4971304
            else:
                if input[0] < 8.0:
                    var118 = 0.89641476
                else:
                    var118 = -0.5163649
    else:
        if input[2] < 2235.72:
            if input[3] < 99.545456:
                if input[1] < 459.0:
                    var118 = 0.1663988
                else:
                    var118 = 1.1371092
            else:
                var118 = 4.0191307
        else:
            if input[1] < 403.0:
                if input[8] < 38.0:
                    var118 = -0.4378235
                else:
                    var118 = 2.2357213
            else:
                if input[8] < 27.0:
                    var118 = -0.24538676
                else:
                    var118 = -1.87705
    if input[8] < 7.0:
        if input[1] < 59.0:
            if input[3] < 2.5:
                var119 = -1.7662944
            else:
                if input[1] < 14.0:
                    var119 = 0.49991304
                else:
                    var119 = -0.36608315
        else:
            if input[2] < 954.02:
                if input[2] < 852.7:
                    var119 = 0.9240136
                else:
                    var119 = -1.2539628
            else:
                if input[2] < 2035.17:
                    var119 = 2.5137022
                else:
                    var119 = -0.27397287
    else:
        if input[8] < 52.0:
            if input[8] < 49.0:
                if input[2] < 1013.03:
                    var119 = -0.42582425
                else:
                    var119 = 0.5735325
            else:
                if input[8] < 50.0:
                    var119 = -11.339568
                else:
                    var119 = -0.61310816
        else:
            if input[8] < 57.0:
                if input[3] < 221.5:
                    var119 = 1.9782585
                else:
                    var119 = -0.28311986
            else:
                if input[8] < 84.0:
                    var119 = 0.38229546
                else:
                    var119 = -0.21903244
    if input[1] < 1175.0:
        if input[8] < 49.0:
            if input[1] < 1139.0:
                if input[4] < 24.540909:
                    var120 = -1.1285655
                else:
                    var120 = 0.4887847
            else:
                if input[0] < 3.0:
                    var120 = 0.8646515
                else:
                    var120 = -3.467215
        else:
            if input[8] < 50.0:
                if input[2] < 716.7:
                    var120 = -3.1211042
                else:
                    var120 = -19.166077
            else:
                if input[4] < 206.61363:
                    var120 = -0.08055859
                else:
                    var120 = 0.55094606
    else:
        if input[0] < 12.0:
            if input[8] < 49.0:
                if input[2] < 1990.0:
                    var120 = 4.028131
                else:
                    var120 = 0.752768
            else:
                if input[3] < 297.33334:
                    var120 = 0.21206462
                else:
                    var120 = 3.430536
        else:
            if input[8] < 17.0:
                var120 = 1.559792
            else:
                var120 = -0.51062775
    if input[0] < 13.0:
        if input[2] < 1164.37:
            if input[3] < 128.33333:
                if input[1] < 793.0:
                    var121 = -0.18425642
                else:
                    var121 = 1.0392679
            else:
                if input[8] < 82.0:
                    var121 = -0.36704233
                else:
                    var121 = -1.5861982
        else:
            if input[0] < 8.0:
                if input[4] < 302.982:
                    var121 = 2.0220816
                else:
                    var121 = 0.3370922
            else:
                if input[0] < 9.0:
                    var121 = -2.097676
                else:
                    var121 = 0.3176921
    else:
        if input[1] < 83.0:
            if input[8] < 44.0:
                if input[3] < 3.5:
                    var121 = 0.42528483
                else:
                    var121 = -0.2046814
            else:
                if input[0] < 14.0:
                    var121 = -1.7783234
                else:
                    var121 = -0.08792522
        else:
            if input[1] < 659.0:
                if input[3] < 47.2:
                    var121 = 1.5845263
                else:
                    var121 = 5.0240436
            else:
                if input[3] < 72.666664:
                    var121 = -0.2821878
                else:
                    var121 = 1.7408472
    if input[0] < 10.0:
        if input[8] < 4.0:
            if input[1] < 672.0:
                if input[3] < 89.22222:
                    var122 = 1.2985611
                else:
                    var122 = -0.81539506
            else:
                if input[0] < 8.0:
                    var122 = 3.9635742
                else:
                    var122 = -1.3741028
        else:
            if input[4] < 316.74667:
                if input[6] < 39.0:
                    var122 = -0.000042196683
                else:
                    var122 = -2.3580463
            else:
                if input[6] < 46.0:
                    var122 = 0.04491343
                else:
                    var122 = 1.6567442
    else:
        if input[3] < 99.545456:
            if input[8] < 95.0:
                if input[8] < 90.0:
                    var122 = 0.3569381
                else:
                    var122 = 2.6130188
            else:
                if input[4] < 53.735:
                    var122 = 0.413548
                else:
                    var122 = -1.324555
        else:
            if input[1] < 1192.0:
                if input[4] < 205.0089:
                    var122 = 3.5403657
                else:
                    var122 = 0.39601645
            else:
                var122 = -1.6135285
    if input[8] < 99.0:
        if input[0] < 11.0:
            if input[8] < 10.0:
                if input[0] < 8.0:
                    var123 = 1.3129276
                else:
                    var123 = -0.46083456
            else:
                if input[8] < 52.0:
                    var123 = -0.41071486
                else:
                    var123 = 0.22315362
        else:
            if input[3] < 99.545456:
                if input[4] < 16.933332:
                    var123 = -1.3012565
                else:
                    var123 = 0.5726269
            else:
                if input[8] < 55.0:
                    var123 = 4.6800337
                else:
                    var123 = 1.6399403
    else:
        if input[2] < 631.88:
            if input[1] < 601.0:
                if input[4] < 70.6:
                    var123 = 0.7066418
                else:
                    var123 = -0.52049714
            else:
                var123 = -1.8895609
        else:
            if input[0] < 5.0:
                var123 = -0.59908754
            else:
                var123 = -4.329366
    if input[8] < 99.0:
        if input[4] < 40.83286:
            if input[8] < 90.0:
                if input[2] < 350.58:
                    var124 = -0.48941842
                else:
                    var124 = -2.4074523
            else:
                if input[4] < 8.236:
                    var124 = 4.681228
                else:
                    var124 = 0.41669354
        else:
            if input[8] < 49.0:
                if input[8] < 27.0:
                    var124 = 0.13331184
                else:
                    var124 = 0.9546878
            else:
                if input[8] < 50.0:
                    var124 = -9.907891
                else:
                    var124 = 0.4286852
    else:
        if input[2] < 631.88:
            if input[3] < 74.416664:
                if input[3] < 28.666666:
                    var124 = -0.3940613
                else:
                    var124 = 0.43168822
            else:
                if input[1] < 147.0:
                    var124 = -0.47035408
                else:
                    var124 = -1.8265747
        else:
            if input[1] < 798.0:
                if input[4] < 109.04143:
                    var124 = -1.2547201
                else:
                    var124 = -3.8491688
            else:
                var124 = -0.58411103
    if input[5] < 2.0:
        if input[0] < 14.0:
            if input[2] < 2462.26:
                if input[2] < 2317.31:
                    var125 = -0.38522705
                else:
                    var125 = -4.3212624
            else:
                var125 = 2.434121
        else:
            if input[2] < 106.86:
                var125 = 4.4399996
            else:
                if input[2] < 449.83:
                    var125 = -0.23357849
                else:
                    var125 = 0.07909546
    else:
        if input[8] < 99.0:
            if input[3] < 9.375:
                if input[3] < 8.2:
                    var125 = -0.1772522
                else:
                    var125 = 2.9194007
            else:
                if input[4] < 8.236:
                    var125 = 1.5507983
                else:
                    var125 = 0.21907201
        else:
            if input[5] < 15.0:
                if input[0] < 12.0:
                    var125 = 0.03507102
                else:
                    var125 = -2.5289109
            else:
                if input[5] < 16.0:
                    var125 = -3.189257
                else:
                    var125 = -0.5742422
    if input[7] < 14.0:
        if input[4] < 28.927143:
            if input[4] < 21.13:
                if input[4] < 16.933332:
                    var126 = -0.55428463
                else:
                    var126 = 1.5250448
            else:
                if input[3] < 47.2:
                    var126 = -0.8249507
                else:
                    var126 = -2.4771938
        else:
            if input[8] < 49.0:
                if input[8] < 48.0:
                    var126 = 0.42562625
                else:
                    var126 = 2.548734
            else:
                if input[8] < 50.0:
                    var126 = -7.1899333
                else:
                    var126 = 0.26846886
    else:
        if input[3] < 491.5:
            if input[8] < 51.0:
                if input[2] < 202.49:
                    var126 = 1.3196472
                else:
                    var126 = -2.2662024
            else:
                if input[2] < 1862.04:
                    var126 = 0.041690417
                else:
                    var126 = -2.5234792
        else:
            if input[7] < 43.0:
                if input[2] < 1690.22:
                    var126 = 0.022197125
                else:
                    var126 = 2.1659057
            else:
                if input[2] < 1549.86:
                    var126 = 0.47338015
                else:
                    var126 = -8.252565
    var127 = var71 + var72 + var73 + var74 + var75 + var76 + var77 + var78 + var79 + var80 + var81 + var82 + var83 + var84 + var85 + var86 + var87 + var88 + var89 + var90 + var91 + var92 + var93 + var94 + var95 + var96 + var97 + var98 + var99 + var100 + var101 + var102 + var103 + var104 + var105 + var106 + var107 + var108 + var109 + var110 + var111 + var112 + var113 + var114 + var115 + var116 + var117 + var118 + var119 + var120 + var121 + var122 + var123 + var124 + var125 + var126
    if input[2] < 749.56:
        if input[0] < 13.0:
            if input[2] < 619.42:
                if input[2] < 347.82:
                    var128 = -0.5152712
                else:
                    var128 = 0.30224514
            else:
                if input[3] < 136.14285:
                    var128 = -0.26962963
                else:
                    var128 = -2.0723965
        else:
            if input[2] < 486.02:
                if input[8] < 70.0:
                    var128 = -1.9250749
                else:
                    var128 = 2.6937866
            else:
                if input[2] < 587.38:
                    var128 = 3.9794178
                else:
                    var128 = -1.0314789
    else:
        if input[2] < 834.06:
            if input[1] < 947.0:
                if input[0] < 14.0:
                    var128 = 1.6903235
                else:
                    var128 = -0.50401
            else:
                var128 = 5.254973
        else:
            if input[0] < 4.0:
                if input[1] < 616.0:
                    var128 = -0.92162037
                else:
                    var128 = 0.2530637
            else:
                if input[0] < 8.0:
                    var128 = 0.9635709
                else:
                    var128 = 0.16952193
    if input[4] < 154.2375:
        if input[2] < 1013.03:
            if input[2] < 863.93:
                if input[3] < 24.09091:
                    var129 = -0.71607995
                else:
                    var129 = 0.3157522
            else:
                if input[2] < 871.76:
                    var129 = -5.8396487
                else:
                    var129 = -1.5553427
        else:
            if input[3] < 95.8:
                if input[2] < 1179.9:
                    var129 = -0.31378856
                else:
                    var129 = 1.2912008
            else:
                if input[1] < 1096.0:
                    var129 = 4.7147555
                else:
                    var129 = 0.8850983
    else:
        if input[2] < 1422.11:
            if input[8] < 65.0:
                if input[2] < 1411.49:
                    var129 = -0.9202793
                else:
                    var129 = -10.061745
            else:
                if input[8] < 82.0:
                    var129 = 1.2964689
                else:
                    var129 = -0.5008144
        else:
            if input[2] < 1516.42:
                if input[1] < 1012.0:
                    var129 = 2.7056174
                else:
                    var129 = -0.7108008
            else:
                if input[8] < 49.0:
                    var129 = 0.3574885
                else:
                    var129 = -0.40540442
    if input[8] < 49.0:
        if input[4] < 26.626667:
            if input[1] < 296.0:
                if input[1] < 66.13:
                    var130 = -0.6534887
                else:
                    var130 = 1.2833776
            else:
                if input[1] < 1006.0:
                    var130 = -2.890329
                else:
                    var130 = -0.23342042
        else:
            if input[3] < 815.0:
                if input[3] < 210.0:
                    var130 = 0.7334652
                else:
                    var130 = -0.5745125
            else:
                if input[2] < 1607.8:
                    var130 = 1.259795
                else:
                    var130 = 3.6662385
    else:
        if input[8] < 50.0:
            if input[2] < 716.7:
                if input[2] < 407.43:
                    var130 = 1.9076718
                else:
                    var130 = -3.90814
            else:
                var130 = -17.168022
        else:
            if input[8] < 81.0:
                if input[4] < 591.365:
                    var130 = 0.58100426
                else:
                    var130 = -0.9766224
            else:
                if input[1] < 781.0:
                    var130 = 0.14952599
                else:
                    var130 = -1.0367348
    if input[0] < 2.0:
        if input[1] < 1086.0:
            if input[1] < 1062.0:
                if input[1] < 483.0:
                    var131 = -1.0002038
                else:
                    var131 = 0.12392717
            else:
                var131 = -7.6132417
        else:
            if input[2] < 927.74:
                if input[1] < 1116.0:
                    var131 = 0.6394633
                else:
                    var131 = -0.8195648
            else:
                if input[2] < 1549.86:
                    var131 = 1.3982483
                else:
                    var131 = 3.615863
    else:
        if input[4] < 316.74667:
            if input[2] < 2273.6:
                if input[2] < 1171.99:
                    var131 = 0.022188976
                else:
                    var131 = 0.4764855
            else:
                if input[1] < 527.0:
                    var131 = 1.1479986
                else:
                    var131 = -2.7709603
        else:
            if input[0] < 4.0:
                if input[7] < 19.0:
                    var131 = -0.3564947
                else:
                    var131 = 1.5971575
            else:
                if input[4] < 562.6275:
                    var131 = 1.1580391
                else:
                    var131 = 3.4195497
    if input[4] < 8.236:
        if input[0] < 3.0:
            var132 = -0.81313175
        else:
            if input[1] < 1182.0:
                if input[0] < 11.0:
                    var132 = 1.5675172
                else:
                    var132 = 4.28428
            else:
                var132 = -0.48328248
    else:
        if input[4] < 28.927143:
            if input[0] < 3.0:
                if input[2] < 21.17:
                    var132 = -0.37253577
                else:
                    var132 = 0.9914007
            else:
                if input[0] < 10.0:
                    var132 = -2.4482484
                else:
                    var132 = -0.9520899
        else:
            if input[1] < 989.0:
                if input[3] < 64.57143:
                    var132 = 0.37250504
                else:
                    var132 = -0.26080647
            else:
                if input[1] < 1038.0:
                    var132 = 1.9382048
                else:
                    var132 = 0.059058376
    if input[1] < 1162.0:
        if input[1] < 1145.0:
            if input[0] < 12.0:
                if input[1] < 72.0:
                    var133 = -0.8754228
                else:
                    var133 = 0.08640476
            else:
                if input[3] < 51.25:
                    var133 = 1.259795
                else:
                    var133 = -0.05937426
        else:
            if input[2] < 2218.74:
                if input[0] < 3.0:
                    var133 = 0.56531984
                else:
                    var133 = -3.0612342
            else:
                if input[0] < 3.0:
                    var133 = 0.22091065
                else:
                    var133 = 1.6717438
    else:
        if input[4] < 95.62:
            if input[4] < 1.9266666:
                var133 = -0.47120056
            else:
                if input[1] < 1175.0:
                    var133 = 1.671167
                else:
                    var133 = 3.8767273
        else:
            if input[2] < 1084.16:
                if input[0] < 3.0:
                    var133 = 1.7490876
                else:
                    var133 = -1.9975294
            else:
                if input[2] < 1901.83:
                    var133 = 2.7240512
                else:
                    var133 = 0.56326526
    if input[4] < 170.74333:
        if input[2] < 1024.53:
            if input[2] < 863.93:
                if input[2] < 735.52:
                    var134 = 0.08457916
                else:
                    var134 = 1.430958
            else:
                if input[8] < 90.0:
                    var134 = -2.4471557
                else:
                    var134 = 0.64446336
        else:
            if input[3] < 103.2:
                if input[2] < 1049.84:
                    var134 = 3.433659
                else:
                    var134 = 0.3743784
            else:
                if input[8] < 5.0:
                    var134 = -1.946811
                else:
                    var134 = 5.2170773
    else:
        if input[0] < 8.0:
            if input[4] < 182.08:
                if input[8] < 75.0:
                    var134 = -1.3491437
                else:
                    var134 = -3.5399494
            else:
                if input[0] < 7.0:
                    var134 = 0.040351268
                else:
                    var134 = 1.5109717
        else:
            if input[3] < 59.0:
                if input[0] < 9.0:
                    var134 = -1.3065814
                else:
                    var134 = 0.3858506
            else:
                if input[1] < 483.0:
                    var134 = -9.404386
                else:
                    var134 = -1.4162734
    if input[1] < 1086.0:
        if input[7] < 43.0:
            if input[8] < 99.0:
                if input[1] < 1070.0:
                    var135 = 0.044124037
                else:
                    var135 = -1.3770913
            else:
                if input[2] < 475.95:
                    var135 = -0.47470078
                else:
                    var135 = -2.8017852
        else:
            var135 = -7.4275575
    else:
        if input[0] < 6.0:
            if input[0] < 3.0:
                if input[4] < 1630.25:
                    var135 = 1.0244166
                else:
                    var135 = 3.5208192
            else:
                if input[3] < 381.0:
                    var135 = -0.06187722
                else:
                    var135 = -2.1395557
        else:
            if input[3] < 95.4:
                if input[1] < 1145.0:
                    var135 = 1.3366333
                else:
                    var135 = -1.6090109
            else:
                if input[4] < 2.850909:
                    var135 = -1.6522827
                else:
                    var135 = 2.0194535
    if input[8] < 49.0:
        if input[6] < 4.0:
            if input[0] < 5.0:
                if input[8] < 27.0:
                    var136 = 1.1342419
                else:
                    var136 = -0.225351
            else:
                if input[8] < 34.0:
                    var136 = -3.5252838
                else:
                    var136 = -0.410619
        else:
            if input[8] < 48.0:
                if input[3] < 815.0:
                    var136 = 0.2894089
                else:
                    var136 = 2.5229633
            else:
                if input[1] < 643.0:
                    var136 = -0.8173416
                else:
                    var136 = 4.0826874
    else:
        if input[8] < 50.0:
            if input[2] < 716.7:
                if input[2] < 407.43:
                    var136 = 2.3460937
                else:
                    var136 = -4.8993335
            else:
                var136 = -16.652174
        else:
            if input[9] < 9.0:
                if input[1] < 1020.0:
                    var136 = -0.29196802
                else:
                    var136 = 0.74641865
            else:
                if input[0] < 8.0:
                    var136 = 0.7456075
                else:
                    var136 = -1.2172264
    if input[8] < 99.0:
        if input[1] < 1100.0:
            if input[7] < 43.0:
                if input[8] < 87.0:
                    var137 = -0.0318636
                else:
                    var137 = 0.609774
            else:
                if input[1] < 1086.0:
                    var137 = -6.825565
                else:
                    var137 = 0.48683473
        else:
            if input[3] < 143.0:
                if input[8] < 44.0:
                    var137 = 3.6218135
                else:
                    var137 = 0.21601258
            else:
                if input[3] < 148.125:
                    var137 = -3.4797394
                else:
                    var137 = 0.49985394
    else:
        if input[6] < 13.0:
            if input[1] < 601.0:
                if input[1] < 534.0:
                    var137 = -0.37767625
                else:
                    var137 = 0.71233827
            else:
                var137 = -1.5852163
        else:
            if input[0] < 5.0:
                var137 = -0.4673767
            else:
                var137 = -3.9124107
    if input[0] < 14.0:
        if input[1] < 597.0:
            if input[1] < 516.0:
                if input[2] < 2104.61:
                    var138 = -0.17429821
                else:
                    var138 = 1.1036476
            else:
                if input[8] < 52.0:
                    var138 = -3.9172413
                else:
                    var138 = -0.5813678
        else:
            if input[4] < 170.74333:
                if input[2] < 1013.03:
                    var138 = 0.059012126
                else:
                    var138 = 1.6646572
            else:
                if input[7] < 4.0:
                    var138 = -1.1338092
                else:
                    var138 = 0.2753998
    else:
        if input[1] < 597.0:
            if input[2] < 106.86:
                var138 = 3.9079397
            else:
                if input[2] < 530.44:
                    var138 = -1.7201325
                else:
                    var138 = 1.9536213
        else:
            if input[8] < 69.0:
                if input[8] < 26.0:
                    var138 = 0.52561104
                else:
                    var138 = -1.9192648
            else:
                if input[8] < 76.0:
                    var138 = 3.9859865
                else:
                    var138 = -0.5393616
    if input[1] < 1175.0:
        if input[8] < 95.0:
            if input[8] < 90.0:
                if input[8] < 84.0:
                    var139 = 0.027184475
                else:
                    var139 = -1.1526549
            else:
                if input[0] < 10.0:
                    var139 = -0.10247069
                else:
                    var139 = 1.780687
        else:
            if input[4] < 8.236:
                if input[2] < 19.76:
                    var139 = 0.03706665
                else:
                    var139 = 2.1896439
            else:
                if input[4] < 239.245:
                    var139 = -1.5595869
                else:
                    var139 = -0.00031681062
    else:
        if input[4] < 2.850909:
            var139 = -1.6075867
        else:
            if input[2] < 1901.83:
                if input[1] < 1187.0:
                    var139 = 3.7075164
                else:
                    var139 = 0.8029168
            else:
                if input[1] < 1187.0:
                    var139 = -0.63897705
                else:
                    var139 = 1.6896546
    if input[9] < 67.0:
        if input[1] < 313.0:
            if input[1] < 286.0:
                if input[0] < 14.0:
                    var140 = -0.09251555
                else:
                    var140 = 1.5736479
            else:
                if input[2] < 484.34:
                    var140 = 0.26782665
                else:
                    var140 = -2.599043
        else:
            if input[1] < 512.0:
                if input[1] < 482.0:
                    var140 = 0.66855866
                else:
                    var140 = 3.3124516
            else:
                if input[1] < 586.0:
                    var140 = -1.1442231
                else:
                    var140 = 0.12732317
    else:
        if input[1] < 1004.0:
            if input[1] < 678.0:
                if input[1] < 45.0:
                    var140 = -0.24862671
                else:
                    var140 = -2.211314
            else:
                if input[1] < 828.0:
                    var140 = 0.4922409
                else:
                    var140 = 1.9939835
        else:
            var140 = -6.6624894
    if input[0] < 14.0:
        if input[1] < 597.0:
            if input[1] < 512.0:
                if input[2] < 2462.26:
                    var141 = -0.14270142
                else:
                    var141 = 3.1071188
            else:
                if input[1] < 522.0:
                    var141 = -5.743058
                else:
                    var141 = -1.1527548
        else:
            if input[3] < 51.25:
                if input[3] < 47.2:
                    var141 = -0.65749514
                else:
                    var141 = 4.960723
            else:
                if input[3] < 99.545456:
                    var141 = -0.3875392
                else:
                    var141 = 0.38678434
    else:
        if input[2] < 2091.79:
            if input[8] < 96.0:
                if input[1] < 1020.0:
                    var141 = 1.3681269
                else:
                    var141 = 3.671023
            else:
                if input[1] < 83.0:
                    var141 = -0.09016724
                else:
                    var141 = -2.3503768
        else:
            if input[8] < 27.0:
                if input[1] < 470.0:
                    var141 = 0.17472534
                else:
                    var141 = 1.1679108
            else:
                if input[8] < 69.0:
                    var141 = -2.1486194
                else:
                    var141 = -0.087032065
    if input[9] < 67.0:
        if input[2] < 1013.03:
            if input[2] < 863.93:
                if input[8] < 10.0:
                    var142 = 0.8435103
                else:
                    var142 = -0.19792232
            else:
                if input[2] < 865.92:
                    var142 = -4.299821
                else:
                    var142 = -0.6722726
        else:
            if input[4] < 150.28334:
                if input[1] < 1009.0:
                    var142 = 0.34415963
                else:
                    var142 = 2.930551
            else:
                if input[0] < 8.0:
                    var142 = 0.44675013
                else:
                    var142 = -0.7327138
    else:
        if input[1] < 1004.0:
            if input[1] < 678.0:
                if input[1] < 45.0:
                    var142 = -0.23558147
                else:
                    var142 = -2.0231621
            else:
                if input[8] < 51.0:
                    var142 = 1.673288
                else:
                    var142 = -0.24393006
        else:
            var142 = -6.505597
    if input[1] < 94.0:
        if input[2] < 2317.31:
            if input[2] < 2152.66:
                if input[2] < 863.93:
                    var143 = -0.19867136
                else:
                    var143 = -0.984678
            else:
                if input[0] < 2.0:
                    var143 = -0.06968384
                else:
                    var143 = 1.5956452
        else:
            if input[2] < 2328.11:
                var143 = -7.5092897
            else:
                if input[1] < 19.0:
                    var143 = -1.4794515
                else:
                    var143 = 1.004921
    else:
        if input[4] < 21.13:
            if input[8] < 16.0:
                if input[0] < 2.0:
                    var143 = 0.19008522
                else:
                    var143 = -2.3943458
            else:
                if input[1] < 1080.0:
                    var143 = 1.8086987
                else:
                    var143 = -0.339883
        else:
            if input[4] < 28.927143:
                if input[0] < 3.0:
                    var143 = 0.73092955
                else:
                    var143 = -1.9173685
            else:
                if input[7] < 12.0:
                    var143 = 0.15914467
                else:
                    var143 = -0.40828568
    if input[3] < 989.0:
        if input[4] < 8.236:
            if input[0] < 11.0:
                if input[1] < 805.0:
                    var144 = 0.9697704
                else:
                    var144 = -2.831269
            else:
                if input[1] < 1182.0:
                    var144 = 3.3829486
                else:
                    var144 = -0.35778198
        else:
            if input[4] < 16.933332:
                if input[0] < 3.0:
                    var144 = 0.20121224
                else:
                    var144 = -2.5468488
            else:
                if input[2] < 373.98:
                    var144 = -0.42023703
                else:
                    var144 = 0.09697168
    else:
        if input[2] < 1291.33:
            if input[2] < 967.0:
                if input[1] < 1096.0:
                    var144 = 1.051574
                else:
                    var144 = 0.2922577
            else:
                var144 = -1.6706787
        else:
            if input[1] < 993.0:
                var144 = 0.7684204
            else:
                if input[2] < 1639.17:
                    var144 = 1.6163987
                else:
                    var144 = 3.7979145
    if input[0] < 3.0:
        if input[1] < 1086.0:
            if input[1] < 1070.0:
                if input[3] < 1035.0:
                    var145 = -0.7173249
                else:
                    var145 = 2.1471508
            else:
                var145 = -6.4276977
        else:
            if input[8] < 44.0:
                var145 = 0.7696045
            else:
                if input[2] < 2013.45:
                    var145 = 3.0789082
                else:
                    var145 = 0.13706665
    else:
        if input[2] < 39.86:
            if input[3] < 92.666664:
                if input[0] < 13.0:
                    var145 = 1.3918839
                else:
                    var145 = -0.3488373
            else:
                var145 = 3.7158527
        else:
            if input[9] < 16.0:
                if input[9] < 15.0:
                    var145 = 0.08663922
                else:
                    var145 = -4.4555354
            else:
                if input[2] < 1957.9:
                    var145 = -0.44678694
                else:
                    var145 = 1.3725543
    if input[3] < 183.8:
        if input[3] < 99.545456:
            if input[3] < 95.8:
                if input[1] < 94.0:
                    var146 = -0.51182634
                else:
                    var146 = 0.21796666
            else:
                if input[2] < 897.4:
                    var146 = -0.5418121
                else:
                    var146 = -3.0241818
        else:
            if input[3] < 106.25:
                if input[1] < 1122.0:
                    var146 = 3.3798854
                else:
                    var146 = -0.03490448
            else:
                if input[4] < 216.87273:
                    var146 = 0.78525794
                else:
                    var146 = -0.18721855
    else:
        if input[2] < 1853.57:
            if input[9] < 72.0:
                if input[3] < 199.66667:
                    var146 = -2.3923566
                else:
                    var146 = -0.35220286
            else:
                var146 = -6.267006
        else:
            if input[7] < 34.0:
                if input[1] < 1020.0:
                    var146 = 0.77338135
                else:
                    var146 = -0.64335084
            else:
                if input[1] < 993.0:
                    var146 = 1.1728109
                else:
                    var146 = 3.631956
    if input[8] < 49.0:
        if input[3] < 815.0:
            if input[8] < 48.0:
                if input[9] < 5.0:
                    var147 = -0.25774416
                else:
                    var147 = 0.36429912
            else:
                if input[2] < 388.5:
                    var147 = -1.6437104
                else:
                    var147 = 4.1379275
        else:
            if input[2] < 1639.17:
                var147 = 1.2154883
            else:
                if input[1] < 875.0:
                    var147 = 0.9627533
                else:
                    var147 = 3.9094894
    else:
        if input[8] < 50.0:
            if input[2] < 716.7:
                if input[2] < 407.43:
                    var147 = 1.3147029
                else:
                    var147 = -4.520352
            else:
                var147 = -15.627553
        else:
            if input[4] < 201.81166:
                if input[1] < 1020.0:
                    var147 = -0.3440619
                else:
                    var147 = 0.92164433
            else:
                if input[1] < 965.0:
                    var147 = 0.63176614
                else:
                    var147 = -0.7155534
    if input[8] < 99.0:
        if input[8] < 52.0:
            if input[8] < 49.0:
                if input[8] < 25.0:
                    var148 = -0.16228276
                else:
                    var148 = 0.53431886
            else:
                if input[6] < 14.0:
                    var148 = -0.15880464
                else:
                    var148 = -6.8212852
        else:
            if input[0] < 2.0:
                if input[6] < 39.0:
                    var148 = -0.45678416
                else:
                    var148 = -2.1880903
            else:
                if input[8] < 58.0:
                    var148 = 1.5592693
                else:
                    var148 = 0.3319795
    else:
        if input[6] < 13.0:
            if input[0] < 7.0:
                if input[1] < 534.0:
                    var148 = -0.33402807
                else:
                    var148 = -1.7626221
            else:
                if input[0] < 10.0:
                    var148 = 0.7380814
                else:
                    var148 = -0.09814453
        else:
            var148 = -3.647822
    if input[8] < 49.0:
        if input[3] < 791.0:
            if input[3] < 341.67667:
                if input[0] < 8.0:
                    var149 = 0.715959
                else:
                    var149 = -0.07974323
            else:
                if input[2] < 202.49:
                    var149 = 1.3768108
                else:
                    var149 = -1.1634283
        else:
            if input[2] < 1639.17:
                if input[2] < 927.74:
                    var149 = 0.2481842
                else:
                    var149 = 1.1594287
            else:
                if input[1] < 875.0:
                    var149 = 0.9427399
                else:
                    var149 = 3.7515519
    else:
        if input[8] < 50.0:
            if input[2] < 716.7:
                if input[2] < 407.43:
                    var149 = 1.5851499
                else:
                    var149 = -3.26241
            else:
                var149 = -13.961936
        else:
            if input[8] < 84.0:
                if input[9] < 78.0:
                    var149 = 0.334103
                else:
                    var149 = -2.1253858
            else:
                if input[8] < 87.0:
                    var149 = -1.306928
                else:
                    var149 = -0.083800375
    if input[1] < 344.0:
        if input[8] < 32.0:
            if input[3] < 37.857143:
                if input[3] < 8.857142:
                    var150 = 0.9509186
                else:
                    var150 = -0.44818267
            else:
                if input[3] < 101.28571:
                    var150 = 1.1266915
                else:
                    var150 = -0.26074484
        else:
            if input[8] < 50.0:
                if input[8] < 49.0:
                    var150 = -0.6132515
                else:
                    var150 = -6.715427
            else:
                if input[9] < 6.0:
                    var150 = -0.4256986
                else:
                    var150 = 0.5616669
    else:
        if input[1] < 389.0:
            if input[2] < 2072.39:
                if input[2] < 311.43:
                    var150 = -0.92971754
                else:
                    var150 = 1.0986668
            else:
                var150 = 4.3796477
        else:
            if input[9] < 80.0:
                if input[2] < 1807.71:
                    var150 = 0.25505418
                else:
                    var150 = -0.36009794
            else:
                if input[1] < 993.0:
                    var150 = 0.69535345
                else:
                    var150 = 3.6108673
    if input[3] < 989.0:
        if input[3] < 356.5:
            if input[1] < 333.0:
                if input[8] < 32.0:
                    var151 = 0.30931824
                else:
                    var151 = -0.31567758
            else:
                if input[1] < 512.0:
                    var151 = 1.12287
                else:
                    var151 = 0.09597559
        else:
            if input[8] < 58.0:
                if input[3] < 532.0:
                    var151 = -1.4548289
                else:
                    var151 = -0.30822274
            else:
                if input[8] < 64.0:
                    var151 = 1.3578522
                else:
                    var151 = -0.25041732
    else:
        if input[2] < 1607.8:
            if input[2] < 1291.33:
                if input[2] < 967.0:
                    var151 = 0.4867508
                else:
                    var151 = -1.6181793
            else:
                var151 = 1.1701797
        else:
            var151 = 3.4754608
    if input[2] < 2385.6:
        if input[1] < 94.0:
            if input[2] < 2248.68:
                if input[2] < 1129.52:
                    var152 = -0.6932169
                else:
                    var152 = 0.30913255
            else:
                if input[0] < 5.0:
                    var152 = -6.259453
                else:
                    var152 = 0.6005463
        else:
            if input[3] < 83.916664:
                if input[8] < 93.0:
                    var152 = 0.52452457
                else:
                    var152 = -0.8296132
            else:
                if input[3] < 87.0:
                    var152 = -3.3335826
                else:
                    var152 = 0.043020394
    else:
        if input[0] < 8.0:
            if input[2] < 2489.69:
                if input[1] < 173.0:
                    var152 = -0.68024427
                else:
                    var152 = 0.3531019
            else:
                var152 = 3.2627351
        else:
            if input[0] < 11.0:
                if input[8] < 34.0:
                    var152 = -5.0864806
                else:
                    var152 = -2.4154563
            else:
                if input[8] < 77.0:
                    var152 = -0.090431355
                else:
                    var152 = -2.079706
    if input[8] < 49.0:
        if input[4] < 131.048:
            if input[2] < 841.11:
                if input[2] < 290.78:
                    var153 = -0.39783826
                else:
                    var153 = 0.65790576
            else:
                if input[2] < 888.24:
                    var153 = -3.5156994
                else:
                    var153 = -0.68613017
        else:
            if input[2] < 2166.02:
                if input[3] < 202.0:
                    var153 = 1.2003816
                else:
                    var153 = -0.09061345
            else:
                if input[4] < 554.7167:
                    var153 = -0.9820452
                else:
                    var153 = 1.5848001
    else:
        if input[8] < 50.0:
            if input[2] < 716.7:
                if input[4] < 38.885:
                    var153 = 3.4260113
                else:
                    var153 = -3.2662284
            else:
                var153 = -13.913777
        else:
            if input[2] < 2367.63:
                if input[6] < 42.0:
                    var153 = 0.0051102806
                else:
                    var153 = 0.9827346
            else:
                if input[1] < 816.0:
                    var153 = -0.1308742
                else:
                    var153 = -1.8464082
    if input[1] < 872.0:
        if input[3] < 95.4:
            if input[0] < 7.0:
                if input[1] < 368.0:
                    var154 = 0.29478133
                else:
                    var154 = 2.8740282
            else:
                if input[0] < 9.0:
                    var154 = -1.285283
                else:
                    var154 = 0.17792253
        else:
            if input[3] < 99.545456:
                if input[0] < 8.0:
                    var154 = -2.0013008
                else:
                    var154 = -4.1780243
            else:
                if input[0] < 7.0:
                    var154 = -0.38599345
                else:
                    var154 = 1.9293766
    else:
        if input[1] < 896.0:
            if input[8] < 4.0:
                var154 = -1.7197541
            else:
                if input[1] < 875.0:
                    var154 = 0.1593272
                else:
                    var154 = 2.7809887
        else:
            if input[2] < 2253.61:
                if input[3] < 145.75:
                    var154 = 0.8486584
                else:
                    var154 = -0.15127127
            else:
                if input[0] < 8.0:
                    var154 = -0.035661735
                else:
                    var154 = -1.9702199
    if input[8] < 51.0:
        if input[8] < 49.0:
            if input[2] < 1164.37:
                if input[5] < 23.0:
                    var155 = -0.21000557
                else:
                    var155 = -2.718455
            else:
                if input[2] < 1990.0:
                    var155 = 0.7475892
                else:
                    var155 = -0.3754937
        else:
            if input[8] < 50.0:
                if input[2] < 716.7:
                    var155 = -1.5300868
                else:
                    var155 = -13.310771
            else:
                if input[0] < 10.0:
                    var155 = 0.3480294
                else:
                    var155 = -2.3468964
    else:
        if input[8] < 99.0:
            if input[8] < 81.0:
                if input[4] < 2026.16:
                    var155 = 0.44126993
                else:
                    var155 = -2.0656765
            else:
                if input[8] < 88.0:
                    var155 = -0.6554907
                else:
                    var155 = 0.30512604
        else:
            if input[4] < 51.16143:
                if input[0] < 4.0:
                    var155 = 0.63561785
                else:
                    var155 = -0.27713165
            else:
                if input[1] < 173.0:
                    var155 = -0.24736176
                else:
                    var155 = -2.9889426
    if input[0] < 14.0:
        if input[1] < 238.0:
            if input[1] < 175.0:
                if input[2] < 2317.31:
                    var156 = -0.06822321
                else:
                    var156 = -1.2401215
            else:
                if input[3] < 27.75:
                    var156 = 0.021452194
                else:
                    var156 = -2.058164
        else:
            if input[1] < 532.0:
                if input[3] < 116.71429:
                    var156 = 0.75126326
                else:
                    var156 = -0.7247041
            else:
                if input[3] < 99.545456:
                    var156 = -0.6724505
                else:
                    var156 = 0.22177243
    else:
        if input[3] < 57.642857:
            if input[1] < 69.0:
                if input[1] < 52.0:
                    var156 = -0.02720642
                else:
                    var156 = -0.2510727
            else:
                if input[1] < 553.0:
                    var156 = 2.6435254
                else:
                    var156 = 0.89416504
        else:
            if input[8] < 70.0:
                if input[8] < 26.0:
                    var156 = 1.0366735
                else:
                    var156 = -2.4565222
            else:
                if input[2] < 1734.56:
                    var156 = 4.43267
                else:
                    var156 = -0.1519755
    if input[4] < 154.2375:
        if input[2] < 1013.03:
            if input[2] < 871.76:
                if input[2] < 735.52:
                    var157 = -0.13656624
                else:
                    var157 = 1.2305212
            else:
                if input[4] < 152.42166:
                    var157 = -1.7223078
                else:
                    var157 = 2.164386
        else:
            if input[3] < 72.666664:
                if input[2] < 1171.99:
                    var157 = -1.0954788
                else:
                    var157 = 0.7576296
            else:
                if input[2] < 1429.04:
                    var157 = 3.2975755
                else:
                    var157 = -1.2349324
    else:
        if input[0] < 8.0:
            if input[0] < 7.0:
                if input[2] < 1880.69:
                    var157 = -0.47120842
                else:
                    var157 = 0.45031062
            else:
                if input[1] < 289.0:
                    var157 = -1.2758782
                else:
                    var157 = 1.957424
        else:
            if input[4] < 241.62714:
                if input[2] < 1820.8:
                    var157 = -1.4811783
                else:
                    var157 = -0.12734528
            else:
                if input[1] < 527.0:
                    var157 = -0.2046515
                else:
                    var157 = -3.856659
    if input[8] < 10.0:
        if input[2] < 2091.79:
            if input[0] < 5.0:
                if input[1] < 1004.0:
                    var158 = -0.60693276
                else:
                    var158 = 1.0537239
            else:
                if input[0] < 8.0:
                    var158 = 2.0609856
                else:
                    var158 = 0.39395523
        else:
            if input[0] < 5.0:
                if input[2] < 2178.16:
                    var158 = 0.19596253
                else:
                    var158 = 1.4667461
            else:
                var158 = -2.3808808
    else:
        if input[8] < 13.0:
            if input[2] < 202.49:
                var158 = -3.5800538
            else:
                if input[2] < 2335.55:
                    var158 = -1.3186802
                else:
                    var158 = 1.070691
        else:
            if input[1] < 1187.0:
                if input[0] < 2.0:
                    var158 = -0.52359676
                else:
                    var158 = 0.09198937
            else:
                if input[2] < 1639.17:
                    var158 = -1.9149048
                else:
                    var158 = 0.009002686
    if input[4] < 8.236:
        if input[0] < 11.0:
            if input[0] < 10.0:
                if input[8] < 68.0:
                    var159 = -0.5854358
                else:
                    var159 = 1.546304
            else:
                var159 = -1.8572296
        else:
            if input[4] < 1.9266666:
                var159 = -0.23554383
            else:
                if input[3] < 3.5:
                    var159 = 0.57099915
                else:
                    var159 = 4.014334
    else:
        if input[2] < 171.32:
            if input[0] < 5.0:
                if input[8] < 25.0:
                    var159 = 0.71217906
                else:
                    var159 = -0.3244372
            else:
                if input[5] < 16.0:
                    var159 = -2.2969718
                else:
                    var159 = -0.024279349
        else:
            if input[8] < 95.0:
                if input[5] < 7.0:
                    var159 = -0.14292885
                else:
                    var159 = 0.19066867
            else:
                if input[4] < 239.245:
                    var159 = -1.1199607
                else:
                    var159 = 0.7747496
    if input[0] < 10.0:
        if input[0] < 8.0:
            if input[2] < 2235.72:
                if input[8] < 2.0:
                    var160 = 1.79389
                else:
                    var160 = -0.14709242
            else:
                if input[0] < 5.0:
                    var160 = 1.2024711
                else:
                    var160 = 0.21711309
        else:
            if input[4] < 155.39333:
                if input[8] < 28.0:
                    var160 = -1.5985965
                else:
                    var160 = 0.5317523
            else:
                if input[3] < 59.5:
                    var160 = -0.26394653
                else:
                    var160 = -2.2242613
    else:
        if input[3] < 99.545456:
            if input[4] < 164.8211:
                if input[5] < 9.0:
                    var160 = -0.28590345
                else:
                    var160 = 0.9401126
            else:
                if input[5] < 18.0:
                    var160 = -0.13375896
                else:
                    var160 = -1.5159591
        else:
            if input[4] < 2.850909:
                var160 = -1.4744599
            else:
                if input[4] < 205.0089:
                    var160 = 3.3029351
                else:
                    var160 = 0.16333008
    if input[4] < 8.236:
        if input[4] < 7.056667:
            if input[3] < 97.6:
                if input[1] < 801.0:
                    var161 = 0.49489424
                else:
                    var161 = -1.9265938
            else:
                if input[0] < 5.0:
                    var161 = -0.20102997
                else:
                    var161 = 3.3910542
        else:
            if input[8] < 95.0:
                if input[1] < 123.0:
                    var161 = 3.8889775
                else:
                    var161 = 0.9971649
            else:
                var161 = 0.5875679
    else:
        if input[4] < 16.933332:
            if input[0] < 3.0:
                if input[1] < 66.13:
                    var161 = -0.6352301
                else:
                    var161 = 0.8023661
            else:
                if input[0] < 14.0:
                    var161 = -2.2890437
                else:
                    var161 = 1.1238556
        else:
            if input[4] < 21.13:
                if input[1] < 85.0:
                    var161 = -1.1486994
                else:
                    var161 = 2.084087
            else:
                if input[4] < 28.927143:
                    var161 = -1.5926185
                else:
                    var161 = -0.018267242
    if input[4] < 8.236:
        if input[8] < 87.0:
            if input[8] < 37.0:
                if input[2] < 21.17:
                    var162 = 0.5857422
                else:
                    var162 = 3.167541
            else:
                if input[0] < 8.0:
                    var162 = 0.63118434
                else:
                    var162 = -0.77048916
        else:
            var162 = 3.573546
    else:
        if input[5] < 4.0:
            if input[2] < 1241.21:
                if input[2] < 1227.21:
                    var162 = -0.5480063
                else:
                    var162 = -4.79023
            else:
                if input[3] < 11.222222:
                    var162 = 0.7783369
                else:
                    var162 = -0.4797359
        else:
            if input[3] < 70.25:
                if input[4] < 231.4943:
                    var162 = 0.1305024
                else:
                    var162 = 1.6055313
            else:
                if input[3] < 72.666664:
                    var162 = -2.0188189
                else:
                    var162 = -0.031805575
    if input[1] < 1166.0:
        if input[1] < 1139.0:
            if input[0] < 14.0:
                if input[4] < 16.933332:
                    var163 = -0.9385522
                else:
                    var163 = -0.050744213
            else:
                if input[2] < 193.05:
                    var163 = 2.850641
                else:
                    var163 = 0.37621978
        else:
            if input[2] < 1871.77:
                if input[8] < 44.0:
                    var163 = 1.3661617
                else:
                    var163 = -1.7997674
            else:
                var163 = -3.134842
    else:
        if input[4] < 95.62:
            if input[0] < 7.0:
                var163 = -0.71896976
            else:
                var163 = 2.6852915
        else:
            if input[2] < 1084.16:
                if input[0] < 3.0:
                    var163 = 1.6512727
                else:
                    var163 = -2.0041225
            else:
                if input[2] < 1901.83:
                    var163 = 2.7048917
                else:
                    var163 = 0.11967861
    if input[8] < 99.0:
        if input[0] < 13.0:
            if input[2] < 2385.6:
                if input[8] < 50.0:
                    var164 = -0.11154385
                else:
                    var164 = 0.2603756
            else:
                if input[0] < 8.0:
                    var164 = 0.4706718
                else:
                    var164 = -2.1548371
        else:
            if input[8] < 30.0:
                if input[8] < 27.0:
                    var164 = 1.1534373
                else:
                    var164 = 4.4950852
            else:
                if input[8] < 70.0:
                    var164 = -0.62769324
                else:
                    var164 = 0.95000565
    else:
        if input[2] < 631.88:
            if input[7] < 3.0:
                if input[2] < 545.84:
                    var164 = 0.088590704
                else:
                    var164 = 0.83492893
            else:
                if input[0] < 5.0:
                    var164 = -0.29133016
                else:
                    var164 = -1.6123017
        else:
            if input[0] < 5.0:
                var164 = -0.22937469
            else:
                var164 = -3.2652452
    if input[7] < 42.0:
        if input[7] < 14.0:
            if input[1] < 17.0:
                if input[0] < 5.0:
                    var165 = 0.2793686
                else:
                    var165 = -1.3730918
            else:
                if input[1] < 516.0:
                    var165 = 0.24582706
                else:
                    var165 = -0.067920975
        else:
            if input[1] < 483.0:
                if input[1] < 389.0:
                    var165 = -0.62085724
                else:
                    var165 = -2.0247133
            else:
                if input[0] < 3.0:
                    var165 = 0.15466487
                else:
                    var165 = -1.5163509
    else:
        if input[2] < 1607.8:
            if input[2] < 863.93:
                if input[1] < 1096.0:
                    var165 = 0.6469411
                else:
                    var165 = -0.7715546
            else:
                var165 = 1.0509903
        else:
            var165 = 3.4899824
    if input[1] < 1100.0:
        if input[1] < 1038.0:
            if input[1] < 1020.0:
                if input[2] < 1448.55:
                    var166 = -0.20251861
                else:
                    var166 = 0.36806503
            else:
                if input[4] < 37.923077:
                    var166 = -2.6246583
                else:
                    var166 = 3.076432
        else:
            if input[4] < 212.40857:
                if input[4] < 19.542856:
                    var166 = 1.6119492
                else:
                    var166 = -0.9291744
            else:
                if input[2] < 1742.62:
                    var166 = -0.8857092
                else:
                    var166 = -3.6524453
    else:
        if input[1] < 1113.0:
            if input[2] < 1448.55:
                var166 = 0.41462097
            else:
                var166 = 3.9027936
        else:
            if input[0] < 9.0:
                if input[1] < 1185.0:
                    var166 = -0.4895168
                else:
                    var166 = 1.8969787
            else:
                if input[4] < 208.32:
                    var166 = 1.7723919
                else:
                    var166 = -2.8685212
    if input[3] < 64.22222:
        if input[3] < 62.0:
            if input[3] < 59.333332:
                if input[2] < 1549.86:
                    var167 = -0.106184565
                else:
                    var167 = 0.68330324
            else:
                if input[3] < 60.636364:
                    var167 = -4.124024
                else:
                    var167 = 0.048139002
        else:
            if input[2] < 470.23:
                var167 = -1.6068436
            else:
                if input[4] < 420.32:
                    var167 = 3.4099412
                else:
                    var167 = 0.22642823
    else:
        if input[3] < 72.666664:
            if input[2] < 388.5:
                if input[3] < 65.5:
                    var167 = -1.354802
                else:
                    var167 = 1.8337449
            else:
                if input[2] < 1164.37:
                    var167 = -3.290427
                else:
                    var167 = -0.76636356
        else:
            if input[2] < 1807.71:
                if input[3] < 145.75:
                    var167 = 0.46192184
                else:
                    var167 = -0.33136076
            else:
                if input[3] < 155.57143:
                    var167 = -1.1283187
                else:
                    var167 = 0.24865396
    if input[4] < 8.236:
        if input[8] < 13.0:
            if input[1] < 83.0:
                var168 = 0.59892195
            else:
                var168 = -1.7752854
        else:
            if input[1] < 94.0:
                if input[3] < 31.4:
                    var168 = 0.584726
                else:
                    var168 = -0.5642433
            else:
                if input[8] < 97.0:
                    var168 = 2.8497593
                else:
                    var168 = 0.15022735
    else:
        if input[4] < 39.6625:
            if input[3] < 21.571428:
                if input[1] < 52.0:
                    var168 = -0.37908822
                else:
                    var168 = -2.6223562
            else:
                if input[3] < 49.333332:
                    var168 = 1.4128776
                else:
                    var168 = -0.59139556
        else:
            if input[4] < 66.496155:
                if input[2] < 555.49:
                    var168 = 0.3888619
                else:
                    var168 = 2.408506
            else:
                if input[4] < 66.75667:
                    var168 = -2.8361022
                else:
                    var168 = 0.0897168
    if input[7] < 40.0:
        if input[9] < 6.0:
            if input[4] < 142.11667:
                if input[1] < 1014.0:
                    var169 = -0.05115183
                else:
                    var169 = 0.903772
            else:
                if input[1] < 470.0:
                    var169 = 0.16389634
                else:
                    var169 = 2.379159
        else:
            if input[0] < 8.0:
                if input[8] < 50.0:
                    var169 = -0.31839392
                else:
                    var169 = 0.46425158
            else:
                if input[3] < 51.25:
                    var169 = 0.25971568
                else:
                    var169 = -1.1647311
    else:
        if input[4] < 1630.25:
            if input[4] < 923.0:
                if input[1] < 1062.0:
                    var169 = 0.59927523
                else:
                    var169 = -0.7339844
            else:
                if input[4] < 935.78:
                    var169 = 0.2492096
                else:
                    var169 = 0.99927855
        else:
            var169 = 3.218573
    if input[1] < 1166.0:
        if input[1] < 1158.0:
            if input[4] < 1191.195:
                if input[3] < 44.11111:
                    var170 = -0.23708251
                else:
                    var170 = 0.13277349
            else:
                if input[8] < 47.0:
                    var170 = 0.06646463
                else:
                    var170 = -1.9083254
        else:
            if input[8] < 67.0:
                var170 = -2.3854737
            else:
                if input[0] < 3.0:
                    var170 = 0.15177308
                else:
                    var170 = -0.5544678
    else:
        if input[4] < 2.850909:
            var170 = -1.7154541
        else:
            if input[8] < 52.0:
                if input[0] < 4.0:
                    var170 = 0.07845052
                else:
                    var170 = 1.8998989
            else:
                if input[0] < 3.0:
                    var170 = 2.2257202
                else:
                    var170 = -0.86524487
    if input[3] < 67.36364:
        if input[3] < 61.0:
            if input[3] < 59.5:
                if input[0] < 12.0:
                    var171 = -0.09976175
                else:
                    var171 = 0.6235394
            else:
                if input[4] < 195.534:
                    var171 = -4.3756385
                else:
                    var171 = 0.8972382
        else:
            if input[4] < 62.18308:
                if input[0] < 6.0:
                    var171 = 0.97516376
                else:
                    var171 = 4.055663
            else:
                if input[6] < 12.0:
                    var171 = -1.5598317
                else:
                    var171 = 1.3819054
    else:
        if input[8] < 89.0:
            if input[7] < 4.0:
                if input[1] < 527.0:
                    var171 = 0.7744619
                else:
                    var171 = -0.99478686
            else:
                if input[0] < 7.0:
                    var171 = -0.28430417
                else:
                    var171 = 0.8079371
        else:
            if input[8] < 91.0:
                if input[3] < 183.8:
                    var171 = 3.2356236
                else:
                    var171 = -0.34974
            else:
                if input[4] < 96.096:
                    var171 = 2.1678016
                else:
                    var171 = -0.59018826
    if input[1] < 94.0:
        if input[2] < 2248.68:
            if input[1] < 80.0:
                if input[4] < 39.6625:
                    var172 = -0.8096722
                else:
                    var172 = 0.02638546
            else:
                if input[2] < 1094.06:
                    var172 = -1.6966599
                else:
                    var172 = -0.11341858
        else:
            if input[0] < 8.0:
                if input[0] < 5.0:
                    var172 = -5.4405503
                else:
                    var172 = -1.3716156
            else:
                if input[0] < 9.0:
                    var172 = 0.5713959
                else:
                    var172 = -0.105975345
    else:
        if input[3] < 9.375:
            if input[0] < 13.0:
                if input[1] < 98.0:
                    var172 = -0.58304137
                else:
                    var172 = 1.9511292
            else:
                var172 = 3.0231788
        else:
            if input[1] < 1162.0:
                if input[1] < 1145.0:
                    var172 = -0.04267365
                else:
                    var172 = -1.7962643
            else:
                if input[0] < 3.0:
                    var172 = 2.696342
                else:
                    var172 = 0.44181725
    if input[8] < 99.0:
        if input[8] < 90.0:
            if input[8] < 49.0:
                if input[8] < 48.0:
                    var173 = 0.07352523
                else:
                    var173 = 1.8617436
            else:
                if input[8] < 50.0:
                    var173 = -4.988779
                else:
                    var173 = 0.010883199
        else:
            if input[8] < 92.0:
                if input[4] < 163.17833:
                    var173 = 3.2531984
                else:
                    var173 = 0.015372044
            else:
                if input[4] < 8.236:
                    var173 = 3.1720932
                else:
                    var173 = 0.034066256
    else:
        if input[2] < 477.17:
            if input[1] < 123.0:
                var173 = 0.5133713
            else:
                if input[0] < 7.0:
                    var173 = -0.44846115
                else:
                    var173 = -0.02615509
        else:
            if input[1] < 482.0:
                var173 = -2.918505
            else:
                if input[0] < 9.0:
                    var173 = -1.8203782
                else:
                    var173 = 0.6360331
    if input[8] < 5.0:
        if input[0] < 8.0:
            if input[0] < 5.0:
                if input[1] < 908.0:
                    var174 = -0.49574837
                else:
                    var174 = 0.9005585
            else:
                if input[1] < 672.0:
                    var174 = 0.9069611
                else:
                    var174 = 2.9425738
        else:
            if input[2] < 497.7:
                if input[0] < 9.0:
                    var174 = -0.6988434
                else:
                    var174 = 1.7074798
            else:
                if input[1] < 756.0:
                    var174 = -0.0568929
                else:
                    var174 = -1.670187
    else:
        if input[3] < 82.166664:
            if input[3] < 79.166664:
                if input[8] < 70.0:
                    var174 = -0.27746758
                else:
                    var174 = 0.3377292
            else:
                if input[0] < 9.0:
                    var174 = -0.66061795
                else:
                    var174 = 2.6784046
        else:
            if input[3] < 87.0:
                if input[1] < 1159.0:
                    var174 = -2.8298416
                else:
                    var174 = -0.3162964
            else:
                if input[7] < 4.0:
                    var174 = -0.9899333
                else:
                    var174 = -0.08822522
    if input[3] < 4.9166665:
        if input[4] < 109.88:
            if input[0] < 5.0:
                var175 = -0.21285935
            else:
                if input[8] < 45.0:
                    var175 = -1.9462737
                else:
                    var175 = -0.88814014
        else:
            if input[8] < 71.0:
                if input[8] < 21.0:
                    var175 = -0.03157593
                else:
                    var175 = -1.3177254
            else:
                var175 = 1.692572
    else:
        if input[8] < 49.0:
            if input[0] < 8.0:
                if input[6] < 30.0:
                    var175 = 0.10634398
                else:
                    var175 = 1.0175933
            else:
                if input[4] < 271.90875:
                    var175 = -0.03913221
                else:
                    var175 = -2.8277786
        else:
            if input[8] < 50.0:
                if input[6] < 15.0:
                    var175 = 0.2917389
                else:
                    var175 = -12.62009
            else:
                if input[4] < 201.81166:
                    var175 = -0.20693353
                else:
                    var175 = 0.39313993
    if input[4] < 1143.58:
        if input[2] < 1179.9:
            if input[2] < 863.93:
                if input[2] < 742.17:
                    var176 = -0.05826893
                else:
                    var176 = 0.7770074
            else:
                if input[2] < 920.48:
                    var176 = -2.4737833
                else:
                    var176 = -0.17509586
        else:
            if input[2] < 1203.1:
                if input[5] < 20.0:
                    var176 = 0.6271617
                else:
                    var176 = 8.060874
            else:
                if input[5] < 16.0:
                    var176 = 0.3061402
                else:
                    var176 = -0.31556657
    else:
        if input[2] < 1378.07:
            var176 = -2.0938904
        else:
            if input[3] < 791.0:
                if input[2] < 2455.53:
                    var176 = -1.0302918
                else:
                    var176 = 1.53938
            else:
                if input[7] < 43.0:
                    var176 = 1.5370771
                else:
                    var176 = -1.735598
    if input[3] < 67.36364:
        if input[3] < 62.0:
            if input[6] < 31.0:
                if input[6] < 28.0:
                    var177 = -0.008451238
                else:
                    var177 = -1.4008325
            else:
                if input[1] < 532.0:
                    var177 = 0.87915796
                else:
                    var177 = -0.4122827
        else:
            if input[3] < 64.22222:
                if input[6] < 10.0:
                    var177 = -1.5329773
                else:
                    var177 = 3.284675
            else:
                if input[3] < 65.77778:
                    var177 = -0.80035746
                else:
                    var177 = 1.6574919
    else:
        if input[7] < 4.0:
            if input[1] < 527.0:
                if input[5] < 7.0:
                    var177 = -0.270648
                else:
                    var177 = 1.6627272
            else:
                if input[0] < 10.0:
                    var177 = -2.0651433
                else:
                    var177 = -0.25397012
        else:
            if input[3] < 103.2:
                if input[8] < 25.0:
                    var177 = 0.017961884
                else:
                    var177 = 3.6135767
            else:
                if input[3] < 104.2:
                    var177 = -2.6970346
                else:
                    var177 = 0.14082295
    if input[8] < 85.0:
        if input[1] < 1086.0:
            if input[1] < 1070.0:
                if input[2] < 1486.86:
                    var178 = -0.048570666
                else:
                    var178 = 0.43600565
            else:
                if input[0] < 10.0:
                    var178 = -3.1561725
                else:
                    var178 = -0.23865357
        else:
            if input[4] < 208.32:
                if input[1] < 1182.0:
                    var178 = 1.9072732
                else:
                    var178 = -0.6162991
            else:
                if input[0] < 3.0:
                    var178 = 1.6648579
                else:
                    var178 = -0.50186586
    else:
        if input[4] < 271.90875:
            if input[4] < 84.632:
                if input[0] < 7.0:
                    var178 = -0.8256081
                else:
                    var178 = 0.55599606
            else:
                if input[0] < 11.0:
                    var178 = -1.5757537
                else:
                    var178 = 0.20739327
        else:
            if input[4] < 302.982:
                var178 = 2.8207595
            else:
                if input[2] < 1422.11:
                    var178 = 1.3767675
                else:
                    var178 = -0.4276243
    if input[8] < 49.0:
        if input[3] < 18.166666:
            if input[1] < 17.0:
                if input[0] < 5.0:
                    var179 = 0.13889669
                else:
                    var179 = -1.7290261
            else:
                if input[1] < 36.0:
                    var179 = 1.0803155
                else:
                    var179 = -0.7444477
        else:
            if input[2] < 967.0:
                if input[8] < 48.0:
                    var179 = -0.15768372
                else:
                    var179 = 3.2153034
            else:
                if input[3] < 173.83333:
                    var179 = 0.7912446
                else:
                    var179 = -0.24213386
    else:
        if input[8] < 50.0:
            if input[2] < 568.58:
                if input[1] < 265.0:
                    var179 = 2.6282618
                else:
                    var179 = -0.9137053
            else:
                if input[2] < 716.7:
                    var179 = -3.6473434
                else:
                    var179 = -11.708089
        else:
            if input[4] < 703.63336:
                if input[4] < 216.29:
                    var179 = -0.08721625
                else:
                    var179 = 0.692272
            else:
                if input[1] < 463.0:
                    var179 = -1.393763
                else:
                    var179 = -0.13674761
    if input[3] < 131.8:
        if input[3] < 126.833336:
            if input[7] < 4.0:
                if input[3] < 95.8:
                    var180 = 0.03153371
                else:
                    var180 = -1.7320169
            else:
                if input[4] < 247.745:
                    var180 = 1.3325838
                else:
                    var180 = -1.2851027
        else:
            if input[8] < 2.0:
                var180 = -1.2561524
            else:
                if input[4] < 89.18643:
                    var180 = 0.48577476
                else:
                    var180 = 4.1798515
    else:
        if input[3] < 141.0:
            if input[1] < 684.0:
                if input[1] < 663.0:
                    var180 = -0.18124513
                else:
                    var180 = 1.0378922
            else:
                if input[8] < 77.0:
                    var180 = -1.7858747
                else:
                    var180 = -4.4921813
        else:
            if input[8] < 19.0:
                if input[3] < 152.8:
                    var180 = -2.697961
                else:
                    var180 = -0.6236612
            else:
                if input[1] < 1038.0:
                    var180 = 0.2039231
                else:
                    var180 = -0.7582602
    if input[8] < 4.0:
        if input[0] < 8.0:
            if input[1] < 672.0:
                if input[3] < 89.22222:
                    var181 = 1.3168366
                else:
                    var181 = -0.73307675
            else:
                if input[0] < 4.0:
                    var181 = 0.31230775
                else:
                    var181 = 3.3072834
        else:
            if input[2] < 497.7:
                if input[0] < 9.0:
                    var181 = -0.58739626
                else:
                    var181 = 1.673472
            else:
                if input[1] < 756.0:
                    var181 = 0.18841378
                else:
                    var181 = -1.5548412
    else:
        if input[4] < 316.74667:
            if input[4] < 302.982:
                if input[9] < 12.0:
                    var181 = -0.07149958
                else:
                    var181 = 1.8330435
            else:
                if input[4] < 309.91626:
                    var181 = -2.8881872
                else:
                    var181 = -0.51786095
        else:
            if input[0] < 4.0:
                if input[3] < 532.0:
                    var181 = -0.41759586
                else:
                    var181 = 0.5012529
            else:
                if input[1] < 793.0:
                    var181 = 1.4426614
                else:
                    var181 = -0.0324334
    if input[8] < 95.0:
        if input[1] < 198.0:
            if input[1] < 195.73:
                if input[4] < 463.0775:
                    var182 = 0.005039869
                else:
                    var182 = -0.9954297
            else:
                if input[0] < 4.0:
                    var182 = -0.4595215
                else:
                    var182 = -7.3144875
        else:
            if input[4] < 38.885:
                if input[1] < 296.0:
                    var182 = 1.834006
                else:
                    var182 = -0.7395033
            else:
                if input[0] < 13.0:
                    var182 = 0.14450546
                else:
                    var182 = 0.9074947
    else:
        if input[1] < 482.0:
            if input[2] < 268.91:
                if input[0] < 5.0:
                    var182 = -0.54058534
                else:
                    var182 = 0.7155955
            else:
                if input[1] < 173.0:
                    var182 = -0.3453121
                else:
                    var182 = -2.4549053
        else:
            if input[2] < 1516.42:
                if input[8] < 99.0:
                    var182 = 1.7955048
                else:
                    var182 = -0.34140322
            else:
                if input[0] < 12.0:
                    var182 = -1.9774525
                else:
                    var182 = -0.4164841
    var183 = var127 + var128 + var129 + var130 + var131 + var132 + var133 + var134 + var135 + var136 + var137 + var138 + var139 + var140 + var141 + var142 + var143 + var144 + var145 + var146 + var147 + var148 + var149 + var150 + var151 + var152 + var153 + var154 + var155 + var156 + var157 + var158 + var159 + var160 + var161 + var162 + var163 + var164 + var165 + var166 + var167 + var168 + var169 + var170 + var171 + var172 + var173 + var174 + var175 + var176 + var177 + var178 + var179 + var180 + var181 + var182
    if input[3] < 67.36364:
        if input[1] < 770.0:
            if input[3] < 60.636364:
                if input[3] < 59.5:
                    var184 = 0.11065807
                else:
                    var184 = -3.049057
            else:
                if input[1] < 668.0:
                    var184 = 1.1528176
                else:
                    var184 = 3.5179932
        else:
            if input[1] < 782.17:
                var184 = -3.1488678
            else:
                if input[2] < 841.11:
                    var184 = 0.7148407
                else:
                    var184 = -1.3451691
    else:
        if input[1] < 697.0:
            if input[0] < 7.0:
                if input[4] < 851.3:
                    var184 = 0.073477805
                else:
                    var184 = -1.4622724
            else:
                if input[8] < 70.0:
                    var184 = -2.9967573
                else:
                    var184 = -1.3539978
        else:
            if input[4] < 219.127:
                if input[2] < 888.24:
                    var184 = -0.21660204
                else:
                    var184 = 0.6744544
            else:
                if input[0] < 8.0:
                    var184 = -0.04546229
                else:
                    var184 = -1.935319
    if input[8] < 49.0:
        if input[3] < 791.0:
            if input[2] < 2166.02:
                if input[4] < 133.09222:
                    var185 = -0.057342596
                else:
                    var185 = 0.59627306
            else:
                if input[4] < 316.74667:
                    var185 = -1.2596469
                else:
                    var185 = 0.5721653
        else:
            if input[2] < 1639.17:
                if input[2] < 927.74:
                    var185 = 0.20930175
                else:
                    var185 = 0.8618213
            else:
                if input[1] < 875.0:
                    var185 = 0.690567
                else:
                    var185 = 3.029637
    else:
        if input[8] < 50.0:
            if input[2] < 716.7:
                if input[2] < 407.43:
                    var185 = 2.8511832
                else:
                    var185 = -3.2496872
            else:
                var185 = -11.260746
        else:
            if input[4] < 208.32:
                if input[4] < 144.71857:
                    var185 = -0.07520966
                else:
                    var185 = -0.88006973
            else:
                if input[1] < 993.0:
                    var185 = 0.44234014
                else:
                    var185 = -0.69755
    if input[7] < 42.0:
        if input[0] < 2.0:
            if input[1] < 483.0:
                if input[1] < 389.0:
                    var186 = -0.2664998
                else:
                    var186 = -1.5833858
            else:
                if input[2] < 1690.22:
                    var186 = -0.5297842
                else:
                    var186 = 0.92404175
        else:
            if input[7] < 19.0:
                if input[7] < 4.0:
                    var186 = -0.055422533
                else:
                    var186 = 0.27409014
            else:
                if input[2] < 1862.04:
                    var186 = 2.3959944
                else:
                    var186 = 0.25689697
    else:
        if input[2] < 1607.8:
            var186 = 0.85617894
        else:
            var186 = 3.1021159
    if input[8] < 49.0:
        if input[2] < 2166.02:
            if input[2] < 1171.99:
                if input[2] < 1094.06:
                    var187 = 0.22937591
                else:
                    var187 = -1.4942985
            else:
                if input[4] < 179.72:
                    var187 = 1.30204
                else:
                    var187 = 0.28750253
        else:
            if input[4] < 465.938:
                if input[8] < 43.0:
                    var187 = -1.4163941
                else:
                    var187 = 2.0385895
            else:
                if input[5] < 21.0:
                    var187 = 1.0966518
                else:
                    var187 = -1.6022247
    else:
        if input[8] < 50.0:
            if input[2] < 716.7:
                if input[4] < 97.89667:
                    var187 = 2.9862363
                else:
                    var187 = -1.5387635
            else:
                var187 = -10.680506
        else:
            if input[4] < 8.236:
                if input[0] < 5.0:
                    var187 = 0.2757902
                else:
                    var187 = 2.5367262
            else:
                if input[2] < 373.98:
                    var187 = -0.7601607
                else:
                    var187 = 0.14800468
    if input[7] < 42.0:
        if input[4] < 1143.58:
            if input[4] < 316.74667:
                if input[4] < 302.982:
                    var188 = -0.006806899
                else:
                    var188 = -2.0006592
            else:
                if input[1] < 170.0:
                    var188 = -0.71153116
                else:
                    var188 = 0.57423204
        else:
            if input[6] < 27.0:
                var188 = -1.9630781
            else:
                if input[3] < 791.0:
                    var188 = -1.0588071
                else:
                    var188 = 0.8274285
    else:
        if input[4] < 1630.25:
            var188 = 0.7844862
        else:
            var188 = 2.9891276
    if input[4] < 8.236:
        if input[4] < 7.056667:
            if input[3] < 107.57143:
                if input[4] < 5.848889:
                    var189 = 1.1841879
                else:
                    var189 = -0.2484544
            else:
                var189 = -1.7037842
        else:
            if input[8] < 95.0:
                if input[3] < 40.692307:
                    var189 = 3.3595402
                else:
                    var189 = 0.89787906
            else:
                var189 = 0.53004456
    else:
        if input[4] < 8.715:
            if input[0] < 2.0:
                var189 = -0.5234503
            else:
                var189 = -2.8271952
        else:
            if input[3] < 44.11111:
                if input[4] < 241.62714:
                    var189 = -0.13022055
                else:
                    var189 = -1.3754348
            else:
                if input[3] < 55.0:
                    var189 = 0.8211365
                else:
                    var189 = -0.104135446
    if input[0] < 8.0:
        if input[0] < 7.0:
            if input[2] < 2109.93:
                if input[8] < 49.0:
                    var190 = 0.18015204
                else:
                    var190 = -0.3767304
            else:
                if input[0] < 4.0:
                    var190 = 0.003696289
                else:
                    var190 = 1.8339894
        else:
            if input[1] < 692.0:
                if input[8] < 32.0:
                    var190 = -1.397951
                else:
                    var190 = 0.37616035
            else:
                if input[8] < 81.0:
                    var190 = 2.8051963
                else:
                    var190 = -0.43243232
    else:
        if input[9] < 10.0:
            if input[3] < 100.6:
                if input[0] < 9.0:
                    var190 = -1.0426131
                else:
                    var190 = -0.078994565
            else:
                if input[8] < 8.0:
                    var190 = -2.5895286
                else:
                    var190 = 1.2749176
        else:
            if input[1] < 527.0:
                if input[2] < 2353.5:
                    var190 = -2.171692
                else:
                    var190 = 1.2106904
            else:
                if input[8] < 60.0:
                    var190 = -3.5137048
                else:
                    var190 = -1.2795166
    if input[8] < 49.0:
        if input[8] < 27.0:
            if input[1] < 553.0:
                if input[1] < 483.0:
                    var191 = 0.12699996
                else:
                    var191 = 3.274821
            else:
                if input[4] < 24.540909:
                    var191 = -2.9821594
                else:
                    var191 = -0.45357347
        else:
            if input[3] < 92.666664:
                if input[3] < 79.6:
                    var191 = 0.2534867
                else:
                    var191 = -1.5030762
            else:
                if input[2] < 1013.03:
                    var191 = 0.26453152
                else:
                    var191 = 1.4283618
    else:
        if input[8] < 50.0:
            if input[2] < 497.7:
                if input[2] < 407.43:
                    var191 = 2.9134285
                else:
                    var191 = -0.6605873
            else:
                if input[2] < 716.7:
                    var191 = -3.3625333
                else:
                    var191 = -10.059682
        else:
            if input[4] < 21.13:
                if input[1] < 85.0:
                    var191 = -0.9433613
                else:
                    var191 = 1.6789931
            else:
                if input[2] < 493.0:
                    var191 = -0.76623064
                else:
                    var191 = 0.055932283
    if input[2] < 863.93:
        if input[4] < 28.927143:
            if input[4] < 21.13:
                if input[0] < 11.0:
                    var192 = -0.35243636
                else:
                    var192 = 0.853718
            else:
                if input[0] < 3.0:
                    var192 = 0.89270145
                else:
                    var192 = -1.4342729
        else:
            if input[3] < 399.0:
                if input[8] < 99.0:
                    var192 = 0.55488205
                else:
                    var192 = -1.147478
            else:
                if input[3] < 532.0:
                    var192 = -1.4526066
                else:
                    var192 = -0.032715954
    else:
        if input[2] < 865.92:
            var192 = -3.9485803
        else:
            if input[2] < 871.76:
                if input[0] < 4.0:
                    var192 = -1.6102966
                else:
                    var192 = 4.5983257
            else:
                if input[4] < 68.04667:
                    var192 = -2.9276328
                else:
                    var192 = -0.078086965
    if input[4] < 8.236:
        if input[4] < 7.056667:
            if input[3] < 97.6:
                if input[1] < 801.0:
                    var193 = 0.5321929
                else:
                    var193 = -1.7799584
            else:
                if input[0] < 5.0:
                    var193 = -0.4038101
                else:
                    var193 = 2.7800803
        else:
            var193 = 2.4709194
    else:
        if input[1] < 1185.0:
            if input[4] < 8.715:
                if input[0] < 2.0:
                    var193 = -0.102659605
                else:
                    var193 = -2.6775706
            else:
                if input[2] < 863.93:
                    var193 = 0.11222478
                else:
                    var193 = -0.1587455
        else:
            if input[2] < 1084.16:
                if input[2] < 1013.03:
                    var193 = 0.53067476
                else:
                    var193 = -1.9527609
            else:
                if input[0] < 11.0:
                    var193 = 2.626417
                else:
                    var193 = 0.21796875
    if input[2] < 1129.52:
        if input[2] < 863.93:
            if input[2] < 749.56:
                if input[2] < 619.42:
                    var194 = -0.062855236
                else:
                    var194 = -0.76103586
            else:
                if input[8] < 99.0:
                    var194 = 1.520707
                else:
                    var194 = -2.0993087
        else:
            if input[3] < 72.666664:
                if input[3] < 64.22222:
                    var194 = -1.0517896
                else:
                    var194 = -4.5463066
            else:
                if input[3] < 94.333336:
                    var194 = 1.408641
                else:
                    var194 = -0.9263067
    else:
        if input[4] < 86.75:
            var194 = 4.250041
        else:
            if input[4] < 153.15:
                if input[3] < 103.2:
                    var194 = 0.47667518
                else:
                    var194 = 3.3511193
            else:
                if input[0] < 8.0:
                    var194 = 0.14558528
                else:
                    var194 = -0.45445034
    if input[1] < 1185.0:
        if input[1] < 1158.0:
            if input[6] < 42.0:
                if input[4] < 170.74333:
                    var195 = 0.11889628
                else:
                    var195 = -0.29596508
            else:
                if input[0] < 8.0:
                    var195 = 0.9316718
                else:
                    var195 = -0.18349895
        else:
            if input[4] < 83.54:
                if input[0] < 9.0:
                    var195 = 0.047027588
                else:
                    var195 = 2.1176393
            else:
                if input[4] < 125.935:
                    var195 = -4.515267
                else:
                    var195 = -0.97233886
    else:
        if input[2] < 477.17:
            if input[1] < 1199.0:
                var195 = -1.6045126
            else:
                var195 = -0.22371319
        else:
            if input[0] < 11.0:
                if input[2] < 1990.0:
                    var195 = 2.8126457
                else:
                    var195 = 0.94816697
            else:
                if input[0] < 13.0:
                    var195 = 0.20060425
                else:
                    var195 = -0.11860352
    if input[3] < 9.375:
        if input[3] < 8.2:
            if input[2] < 863.93:
                if input[1] < 19.0:
                    var196 = -0.022209676
                else:
                    var196 = 1.6231152
            else:
                if input[2] < 1210.87:
                    var196 = -1.0777878
                else:
                    var196 = 0.17154062
        else:
            if input[1] < 11.0:
                var196 = -0.18793641
            else:
                if input[2] < 507.59:
                    var196 = 0.10372925
                else:
                    var196 = 2.5016272
    else:
        if input[8] < 81.0:
            if input[8] < 80.0:
                if input[4] < 252.57286:
                    var196 = 0.046605185
                else:
                    var196 = -0.3523332
            else:
                if input[1] < 798.0:
                    var196 = 0.034672037
                else:
                    var196 = 2.7300222
        else:
            if input[1] < 781.0:
                if input[4] < 221.094:
                    var196 = -0.46428472
                else:
                    var196 = 0.6862656
            else:
                if input[4] < 130.638:
                    var196 = 0.28475937
                else:
                    var196 = -1.4316915
    if input[3] < 145.75:
        if input[3] < 142.5:
            if input[3] < 136.14285:
                if input[3] < 126.833336:
                    var197 = -0.04561437
                else:
                    var197 = 1.5005597
            else:
                if input[1] < 275.0:
                    var197 = 0.12682438
                else:
                    var197 = -1.8315314
        else:
            if input[4] < 216.87273:
                if input[1] < 858.0:
                    var197 = 0.9357163
                else:
                    var197 = 6.5249343
            else:
                if input[8] < 28.0:
                    var197 = -2.1203353
                else:
                    var197 = 1.4775422
    else:
        if input[2] < 1690.22:
            if input[2] < 555.49:
                if input[2] < 456.24:
                    var197 = -0.3647255
                else:
                    var197 = 1.009724
            else:
                if input[8] < 92.0:
                    var197 = -1.0184287
                else:
                    var197 = 1.2767094
        else:
            if input[1] < 1038.0:
                if input[1] < 463.0:
                    var197 = -1.5522034
                else:
                    var197 = 1.0671209
            else:
                if input[1] < 1199.0:
                    var197 = -1.1429133
                else:
                    var197 = 2.2907898
    if input[4] < 8.236:
        if input[1] < 59.0:
            if input[4] < 4.44:
                if input[2] < 5.78:
                    var198 = -0.6803261
                else:
                    var198 = 0.4790512
            else:
                var198 = -1.0033184
        else:
            if input[1] < 1182.0:
                if input[1] < 94.0:
                    var198 = 0.47266942
                else:
                    var198 = 2.3254392
            else:
                if input[1] < 1199.0:
                    var198 = -1.7187073
                else:
                    var198 = -0.2150055
    else:
        if input[3] < 1068.0:
            if input[4] < 1143.58:
                if input[1] < 1038.0:
                    var198 = 0.00979248
                else:
                    var198 = -0.46000978
            else:
                if input[9] < 85.0:
                    var198 = -1.2217647
                else:
                    var198 = 0.5604635
        else:
            if input[2] < 1448.55:
                if input[2] < 863.93:
                    var198 = -0.2724243
                else:
                    var198 = 0.6918411
            else:
                var198 = 2.9020915
    if input[7] < 42.0:
        if input[1] < 17.0:
            if input[8] < 71.0:
                if input[3] < 3.5:
                    var199 = -1.6131909
                else:
                    var199 = -0.3976865
            else:
                if input[8] < 91.0:
                    var199 = 1.4578267
                else:
                    var199 = -0.44003296
        else:
            if input[3] < 112.44444:
                if input[7] < 4.0:
                    var199 = -0.023044128
                else:
                    var199 = 1.5079592
            else:
                if input[8] < 76.0:
                    var199 = -0.040623497
                else:
                    var199 = -0.67199844
    else:
        if input[2] < 1607.8:
            if input[8] < 1.0:
                var199 = 0.21758728
            else:
                var199 = 0.85283464
        else:
            var199 = 2.4671419
    if input[8] < 52.0:
        if input[8] < 49.0:
            if input[3] < 815.0:
                if input[3] < 369.66666:
                    var200 = 0.06584479
                else:
                    var200 = -0.89393836
            else:
                if input[2] < 1448.55:
                    var200 = 0.3297628
                else:
                    var200 = 2.060084
        else:
            if input[2] < 1059.79:
                if input[1] < 566.0:
                    var200 = 0.8498532
                else:
                    var200 = -1.512796
            else:
                if input[8] < 50.0:
                    var200 = -9.768125
                else:
                    var200 = -1.3343128
    else:
        if input[8] < 57.0:
            if input[0] < 4.0:
                if input[8] < 55.0:
                    var200 = -0.9248459
                else:
                    var200 = 1.1707067
            else:
                if input[1] < 597.0:
                    var200 = 0.7353096
                else:
                    var200 = 2.469621
        else:
            if input[1] < 774.0:
                if input[1] < 756.0:
                    var200 = 0.18136339
                else:
                    var200 = 2.4015687
            else:
                if input[0] < 12.0:
                    var200 = -0.034704298
                else:
                    var200 = -1.5335416
    if input[0] < 10.0:
        if input[0] < 8.0:
            if input[0] < 7.0:
                if input[2] < 2462.26:
                    var201 = -0.050650854
                else:
                    var201 = 2.0638788
            else:
                if input[3] < 107.57143:
                    var201 = -0.45491782
                else:
                    var201 = 2.0977771
        else:
            if input[4] < 258.2443:
                if input[4] < 73.22462:
                    var201 = 0.49104562
                else:
                    var201 = -0.59020174
            else:
                if input[8] < 34.0:
                    var201 = -3.4803197
                else:
                    var201 = -1.1956627
    else:
        if input[3] < 99.545456:
            if input[4] < 188.31:
                if input[8] < 30.0:
                    var201 = 0.7948145
                else:
                    var201 = 0.038369022
            else:
                if input[8] < 43.0:
                    var201 = -1.4975945
                else:
                    var201 = 0.16113211
        else:
            if input[2] < 271.93:
                var201 = -2.0472047
            else:
                if input[8] < 4.0:
                    var201 = -0.7687073
                else:
                    var201 = 2.931368
    if input[4] < 1191.195:
        if input[8] < 52.0:
            if input[8] < 49.0:
                if input[1] < 1038.0:
                    var202 = 0.14288388
                else:
                    var202 = -0.9033521
            else:
                if input[2] < 1059.79:
                    var202 = -0.021740964
                else:
                    var202 = -7.9761324
        else:
            if input[8] < 58.0:
                if input[4] < 173.92125:
                    var202 = 0.093500234
                else:
                    var202 = 1.6826981
            else:
                if input[4] < 231.4943:
                    var202 = -0.03414415
                else:
                    var202 = 0.4737571
    else:
        if input[1] < 1086.0:
            if input[1] < 1046.0:
                if input[3] < 491.5:
                    var202 = -1.5202937
                else:
                    var202 = -0.26655707
            else:
                var202 = -2.9241486
        else:
            if input[1] < 1113.0:
                var202 = 2.3552277
            else:
                var202 = 0.16191407
    if input[2] < 373.98:
        if input[5] < 8.0:
            if input[8] < 51.0:
                if input[8] < 49.0:
                    var203 = 0.40042406
                else:
                    var203 = 2.7090745
            else:
                if input[2] < 128.94:
                    var203 = 0.4251531
                else:
                    var203 = -1.1407033
        else:
            if input[5] < 16.0:
                if input[3] < 158.8:
                    var203 = -1.8593988
                else:
                    var203 = -0.13468419
            else:
                if input[3] < 78.25:
                    var203 = 2.2286987
                else:
                    var203 = -0.20623267
    else:
        if input[3] < 44.5:
            if input[3] < 38.95:
                if input[3] < 37.857143:
                    var203 = -0.15162557
                else:
                    var203 = 2.5549743
            else:
                if input[3] < 39.642:
                    var203 = -4.5666904
                else:
                    var203 = -0.60384893
        else:
            if input[4] < 97.79667:
                if input[3] < 72.666664:
                    var203 = -0.66276884
                else:
                    var203 = 1.4444594
            else:
                if input[3] < 56.636364:
                    var203 = 1.0233144
                else:
                    var203 = -0.10228684
    if input[3] < 1035.0:
        if input[4] < 71.902:
            if input[4] < 70.6:
                if input[3] < 41.5:
                    var204 = -0.22501257
                else:
                    var204 = 0.44347045
            else:
                if input[1] < 131.0:
                    var204 = 1.2033386
                else:
                    var204 = 3.7300282
        else:
            if input[2] < 393.25:
                if input[2] < 330.29:
                    var204 = -0.27820572
                else:
                    var204 = -1.5434651
            else:
                if input[0] < 8.0:
                    var204 = 0.092569456
                else:
                    var204 = -0.22819315
    else:
        if input[2] < 1607.8:
            var204 = 0.7309246
        else:
            var204 = 2.6690288
    if input[3] < 77.583336:
        if input[1] < 1020.0:
            if input[1] < 1004.0:
                if input[3] < 76.333336:
                    var205 = -0.004189351
                else:
                    var205 = 1.7555088
            else:
                var205 = -2.780607
        else:
            if input[1] < 1025.03:
                var205 = 4.6653137
            else:
                var205 = 0.5106842
    else:
        if input[7] < 4.0:
            if input[1] < 527.0:
                if input[4] < 375.698:
                    var205 = 1.2412724
                else:
                    var205 = -0.45854568
            else:
                if input[4] < 194.44112:
                    var205 = -0.68940914
                else:
                    var205 = -2.358232
        else:
            if input[0] < 7.0:
                if input[3] < 104.2:
                    var205 = -5.202189
                else:
                    var205 = -0.25759777
            else:
                if input[2] < 1742.62:
                    var205 = 1.4082483
                else:
                    var205 = -0.4347301
    if input[7] < 40.0:
        if input[2] < 2489.69:
            if input[4] < 1143.58:
                if input[0] < 14.0:
                    var206 = -0.010640772
                else:
                    var206 = 0.48728472
            else:
                if input[3] < 491.5:
                    var206 = -1.2262443
                else:
                    var206 = -0.15780984
        else:
            if input[0] < 7.0:
                var206 = 2.6183305
            else:
                if input[1] < 868.0:
                    var206 = -0.46182457
                else:
                    var206 = 0.49791566
    else:
        if input[2] < 1549.86:
            if input[8] < 51.0:
                if input[1] < 1116.0:
                    var206 = 0.14859009
                else:
                    var206 = -0.7750244
            else:
                var206 = 0.7812538
        else:
            if input[2] < 1639.17:
                var206 = 0.9361267
            else:
                var206 = 2.4578645
    if input[8] < 4.0:
        if input[0] < 8.0:
            if input[4] < 349.68857:
                if input[4] < 187.2825:
                    var207 = 0.7396741
                else:
                    var207 = 2.8987584
            else:
                if input[0] < 2.0:
                    var207 = -0.196698
                else:
                    var207 = -1.3350343
        else:
            if input[4] < 40.83286:
                if input[0] < 9.0:
                    var207 = -0.55000764
                else:
                    var207 = 1.5895275
            else:
                if input[1] < 296.0:
                    var207 = 0.11326033
                else:
                    var207 = -1.2333657
    else:
        if input[6] < 42.0:
            if input[1] < 601.0:
                if input[1] < 560.0:
                    var207 = -0.24461232
                else:
                    var207 = -2.1012337
            else:
                if input[1] < 633.0:
                    var207 = 1.5720373
                else:
                    var207 = -0.11520598
        else:
            if input[8] < 44.0:
                if input[4] < 316.74667:
                    var207 = -1.1872189
                else:
                    var207 = 0.6290149
            else:
                if input[3] < 63.1:
                    var207 = 1.2005987
                else:
                    var207 = 0.13203299
    if input[3] < 136.14285:
        if input[3] < 126.833336:
            if input[3] < 126.0:
                if input[0] < 7.0:
                    var208 = 0.4117662
                else:
                    var208 = -0.032232586
            else:
                if input[1] < 1012.0:
                    var208 = -0.6824066
                else:
                    var208 = -2.7549703
        else:
            if input[1] < 891.0:
                if input[0] < 6.0:
                    var208 = 1.1553539
                else:
                    var208 = -1.3547109
            else:
                if input[1] < 1166.0:
                    var208 = 3.7328002
                else:
                    var208 = 0.08690186
    else:
        if input[3] < 141.0:
            if input[1] < 836.0:
                if input[8] < 65.0:
                    var208 = -1.4431478
                else:
                    var208 = 0.394981
            else:
                if input[0] < 8.0:
                    var208 = -3.8593056
                else:
                    var208 = -0.6437887
        else:
            if input[6] < 34.0:
                if input[8] < 92.0:
                    var208 = -0.44884402
                else:
                    var208 = 0.92833674
            else:
                if input[1] < 1070.0:
                    var208 = 0.7785572
                else:
                    var208 = -0.46206793
    if input[5] < 4.0:
        if input[3] < 39.642:
            if input[3] < 37.205:
                if input[2] < 1210.87:
                    var209 = -0.63112646
                else:
                    var209 = 0.11139145
            else:
                var209 = -5.7261024
        else:
            if input[3] < 46.142857:
                if input[3] < 45.090908:
                    var209 = 0.92207545
                else:
                    var209 = 3.4716613
            else:
                if input[0] < 2.0:
                    var209 = -0.77197254
                else:
                    var209 = 0.16668786
    else:
        if input[8] < 9.0:
            if input[8] < 8.0:
                if input[0] < 8.0:
                    var209 = 1.2113866
                else:
                    var209 = -0.43321547
            else:
                if input[0] < 11.0:
                    var209 = 3.168119
                else:
                    var209 = -1.2402893
        else:
            if input[8] < 12.0:
                if input[8] < 10.0:
                    var209 = 0.2291687
                else:
                    var209 = -2.089066
            else:
                if input[2] < 2419.86:
                    var209 = 0.12652181
                else:
                    var209 = -0.89472455
    if input[3] < 131.8:
        if input[3] < 128.33333:
            if input[1] < 1100.0:
                if input[1] < 516.0:
                    var210 = 0.24513865
                else:
                    var210 = -0.15430044
            else:
                if input[3] < 115.75:
                    var210 = 1.6208557
                else:
                    var210 = -2.6853547
        else:
            if input[1] < 1158.0:
                var210 = 3.6897328
            else:
                var210 = 0.081567384
    else:
        if input[2] < 1164.37:
            if input[1] < 629.0:
                if input[1] < 508.0:
                    var210 = -0.042857822
                else:
                    var210 = 1.4915134
            else:
                if input[2] < 834.06:
                    var210 = -0.4435146
                else:
                    var210 = -1.978961
        else:
            if input[2] < 1191.4:
                var210 = 5.7301435
            else:
                if input[1] < 483.0:
                    var210 = -1.3905282
                else:
                    var210 = 0.28910008
    if input[1] < 403.0:
        if input[1] < 368.0:
            if input[1] < 296.0:
                if input[1] < 259.96:
                    var211 = -0.002991921
                else:
                    var211 = 1.3281676
            else:
                if input[4] < 188.31:
                    var211 = -1.1300343
                else:
                    var211 = 0.45050913
        else:
            if input[8] < 40.0:
                if input[4] < 187.2825:
                    var211 = -0.6870684
                else:
                    var211 = 1.574502
            else:
                if input[3] < 39.642:
                    var211 = 0.8595886
                else:
                    var211 = 3.572127
    else:
        if input[7] < 4.0:
            if input[3] < 95.4:
                if input[3] < 40.166668:
                    var211 = 0.98409873
                else:
                    var211 = -0.41384363
            else:
                if input[4] < 149.13777:
                    var211 = -0.522492
                else:
                    var211 = -2.7176087
        else:
            if input[3] < 103.2:
                if input[8] < 23.0:
                    var211 = 0.5551788
                else:
                    var211 = 3.1202836
            else:
                if input[8] < 47.0:
                    var211 = 0.44417277
                else:
                    var211 = -0.3461825
    if input[3] < 99.545456:
        if input[3] < 95.8:
            if input[5] < 15.0:
                if input[5] < 7.0:
                    var212 = -0.17026536
                else:
                    var212 = 0.24793719
            else:
                if input[5] < 16.0:
                    var212 = -1.9919604
                else:
                    var212 = -0.32289016
        else:
            if input[0] < 10.0:
                if input[2] < 863.93:
                    var212 = -0.5283712
                else:
                    var212 = -2.9036307
            else:
                if input[0] < 11.0:
                    var212 = -0.7525004
                else:
                    var212 = 0.20753174
    else:
        if input[0] < 7.0:
            if input[3] < 104.2:
                if input[0] < 4.0:
                    var212 = 0.003435262
                else:
                    var212 = -10.8295965
            else:
                if input[0] < 6.0:
                    var212 = 0.07631405
                else:
                    var212 = -1.077161
        else:
            if input[5] < 21.0:
                if input[2] < 1742.62:
                    var212 = 2.4301226
                else:
                    var212 = -0.44790956
            else:
                if input[8] < 28.0:
                    var212 = -1.1716453
                else:
                    var212 = 0.69701666
    if input[8] < 97.0:
        if input[0] < 13.0:
            if input[8] < 32.0:
                if input[0] < 8.0:
                    var213 = 0.13894914
                else:
                    var213 = -0.9511787
            else:
                if input[8] < 46.0:
                    var213 = 0.49733463
                else:
                    var213 = -0.000004370188
        else:
            if input[3] < 72.666664:
                if input[3] < 55.0:
                    var213 = 0.5474212
                else:
                    var213 = -1.1785237
            else:
                if input[4] < 25.788:
                    var213 = -1.5949906
                else:
                    var213 = 2.5652788
    else:
        if input[3] < 58.153847:
            if input[1] < 173.0:
                if input[4] < 8.236:
                    var213 = 0.5151917
                else:
                    var213 = -0.33457017
            else:
                if input[4] < 59.545:
                    var213 = -0.6267975
                else:
                    var213 = -2.7783244
        else:
            if input[6] < 31.0:
                if input[4] < 98.685555:
                    var213 = -0.270849
                else:
                    var213 = 1.8014857
            else:
                if input[6] < 36.0:
                    var213 = -1.8236471
                else:
                    var213 = -0.24203339
    if input[1] < 904.0:
        if input[1] < 875.0:
            if input[2] < 2077.07:
                if input[4] < 375.698:
                    var214 = 0.025651285
                else:
                    var214 = -0.6143057
            else:
                if input[2] < 2183.11:
                    var214 = 1.2639898
                else:
                    var214 = 0.11791152
        else:
            if input[2] < 1963.41:
                if input[1] < 893.0:
                    var214 = 2.4702556
                else:
                    var214 = 0.7476003
            else:
                if input[0] < 6.0:
                    var214 = 0.16449381
                else:
                    var214 = -1.389978
    else:
        if input[7] < 19.0:
            if input[4] < 254.578:
                if input[4] < 73.22462:
                    var214 = -1.1447203
                else:
                    var214 = 0.11345377
            else:
                if input[1] < 1192.0:
                    var214 = -1.4430627
                else:
                    var214 = 1.0458924
        else:
            if input[7] < 43.0:
                if input[2] < 696.14:
                    var214 = -0.028484344
                else:
                    var214 = 1.5940747
            else:
                if input[1] < 1086.0:
                    var214 = -2.9594314
                else:
                    var214 = 0.20700887
    if input[2] < 1147.89:
        if input[6] < 21.0:
            if input[2] < 1013.03:
                if input[2] < 863.93:
                    var215 = 0.04277758
                else:
                    var215 = -0.65259475
            else:
                if input[1] < 692.0:
                    var215 = -0.99527997
                else:
                    var215 = 3.17991
        else:
            if input[3] < 142.5:
                if input[0] < 4.0:
                    var215 = 1.4227768
                else:
                    var215 = -0.7520857
            else:
                var215 = -2.9023988
    else:
        if input[2] < 1210.87:
            if input[1] < 822.0:
                if input[3] < 52.57143:
                    var215 = 1.9235483
                else:
                    var215 = -0.23410721
            else:
                if input[0] < 4.0:
                    var215 = 1.48325
                else:
                    var215 = 6.1680126
        else:
            if input[8] < 49.0:
                if input[3] < 173.83333:
                    var215 = 0.5117962
                else:
                    var215 = -0.2874854
            else:
                if input[8] < 50.0:
                    var215 = -9.517573
                else:
                    var215 = 0.04800957
    if input[3] < 22.556667:
        if input[4] < 39.6625:
            if input[1] < 52.0:
                if input[1] < 32.0:
                    var216 = -1.0145053
                else:
                    var216 = 0.6423569
            else:
                if input[8] < 96.0:
                    var216 = -2.5545223
                else:
                    var216 = -0.17367554
        else:
            if input[1] < 250.0:
                if input[4] < 582.37:
                    var216 = -0.2649547
                else:
                    var216 = 1.2515427
            else:
                var216 = 2.501703
    else:
        if input[1] < 1185.0:
            if input[3] < 131.8:
                if input[7] < 4.0:
                    var216 = 0.1065919
                else:
                    var216 = 0.895116
            else:
                if input[3] < 141.0:
                    var216 = -1.3531884
                else:
                    var216 = 0.062027402
        else:
            if input[4] < 37.923077:
                var216 = -1.3703389
            else:
                if input[4] < 252.57286:
                    var216 = 0.76622653
                else:
                    var216 = 2.588256
    if input[4] < 71.902:
        if input[4] < 40.83286:
            if input[4] < 14.758572:
                if input[4] < 7.056667:
                    var217 = -0.05523
                else:
                    var217 = 1.2744837
            else:
                if input[8] < 98.0:
                    var217 = -0.6426129
                else:
                    var217 = 2.62977
        else:
            if input[1] < 477.0:
                if input[1] < 152.0:
                    var217 = 1.0639185
                else:
                    var217 = -0.21411891
            else:
                if input[4] < 64.46167:
                    var217 = 1.1114041
                else:
                    var217 = 2.8789957
    else:
        if input[6] < 14.0:
            if input[6] < 13.0:
                if input[8] < 25.0:
                    var217 = 0.4398458
                else:
                    var217 = -0.4092299
            else:
                if input[8] < 20.0:
                    var217 = 0.17131601
                else:
                    var217 = -3.5876844
        else:
            if input[6] < 17.0:
                if input[1] < 690.0:
                    var217 = 0.27012748
                else:
                    var217 = 1.9297341
            else:
                if input[6] < 18.0:
                    var217 = -1.1702312
                else:
                    var217 = 0.00385104
    if input[0] < 13.0:
        if input[8] < 50.0:
            if input[8] < 49.0:
                if input[4] < 93.88143:
                    var218 = -0.57350296
                else:
                    var218 = 0.05742079
            else:
                if input[2] < 497.7:
                    var218 = 1.0763732
                else:
                    var218 = -7.7083635
        else:
            if input[3] < 45.090908:
                if input[1] < 175.0:
                    var218 = -0.027585993
                else:
                    var218 = -1.0996542
            else:
                if input[1] < 140.0:
                    var218 = -1.5090151
                else:
                    var218 = 0.25543854
    else:
        if input[8] < 96.0:
            if input[8] < 21.0:
                if input[2] < 841.11:
                    var218 = 1.0247945
                else:
                    var218 = -1.0853828
            else:
                if input[8] < 29.0:
                    var218 = 2.0771532
                else:
                    var218 = 0.42417333
        else:
            if input[8] < 99.0:
                if input[0] < 14.0:
                    var218 = -0.44431305
                else:
                    var218 = -0.08731588
            else:
                var218 = -1.8805786
    if input[8] < 50.0:
        if input[8] < 49.0:
            if input[1] < 532.0:
                if input[1] < 379.0:
                    var219 = -0.018336471
                else:
                    var219 = 1.4314243
            else:
                if input[7] < 4.0:
                    var219 = -0.71849716
                else:
                    var219 = 0.14973252
        else:
            if input[2] < 497.7:
                if input[0] < 3.0:
                    var219 = 0.34723467
                else:
                    var219 = 2.9667633
            else:
                if input[4] < 142.11667:
                    var219 = -1.838314
                else:
                    var219 = -7.471471
    else:
        if input[4] < 231.4943:
            if input[7] < 6.0:
                if input[8] < 58.0:
                    var219 = 0.9816682
                else:
                    var219 = 0.010434305
            else:
                if input[4] < 135.67334:
                    var219 = -1.5975393
                else:
                    var219 = 0.4110311
        else:
            if input[0] < 8.0:
                if input[4] < 252.57286:
                    var219 = 2.9009573
                else:
                    var219 = 0.43071666
            else:
                if input[2] < 2072.39:
                    var219 = 0.6686722
                else:
                    var219 = -1.6415045
    if input[1] < 586.0:
        if input[1] < 516.0:
            if input[4] < 492.1575:
                if input[4] < 189.40462:
                    var220 = -0.14665379
                else:
                    var220 = 0.67726445
            else:
                if input[0] < 3.0:
                    var220 = -1.263139
                else:
                    var220 = -0.26378527
        else:
            if input[2] < 1862.04:
                if input[4] < 162.135:
                    var220 = -1.2384022
                else:
                    var220 = 1.1089035
            else:
                if input[1] < 522.0:
                    var220 = -9.948542
                else:
                    var220 = -1.3613064
    else:
        if input[8] < 89.0:
            if input[8] < 76.0:
                if input[3] < 51.25:
                    var220 = 2.5605059
                else:
                    var220 = 0.19385898
            else:
                if input[2] < 1607.8:
                    var220 = -1.2752471
                else:
                    var220 = 0.05879832
        else:
            if input[2] < 1422.11:
                if input[8] < 99.0:
                    var220 = 2.1164742
                else:
                    var220 = -0.013521467
            else:
                if input[2] < 1916.03:
                    var220 = -1.2845334
                else:
                    var220 = 0.42535767
    if input[1] < 904.0:
        if input[1] < 891.0:
            if input[8] < 93.0:
                if input[8] < 90.0:
                    var221 = 0.036803402
                else:
                    var221 = 1.4513147
            else:
                if input[4] < 8.236:
                    var221 = 1.7688197
                else:
                    var221 = -0.5883051
        else:
            if input[0] < 9.0:
                if input[0] < 2.0:
                    var221 = -0.16828309
                else:
                    var221 = 3.010739
            else:
                var221 = -2.0543823
    else:
        if input[2] < 1285.82:
            if input[2] < 888.24:
                if input[2] < 818.99:
                    var221 = 0.16119033
                else:
                    var221 = -2.6478722
            else:
                if input[0] < 7.0:
                    var221 = -0.08192261
                else:
                    var221 = 3.4055665
        else:
            if input[1] < 934.0:
                if input[8] < 42.0:
                    var221 = -3.2440522
                else:
                    var221 = -0.7896088
            else:
                if input[1] < 1192.0:
                    var221 = -0.4522646
                else:
                    var221 = 1.9936829
    if input[4] < 40.83286:
        if input[3] < 18.166666:
            if input[1] < 47.0:
                if input[1] < 32.0:
                    var222 = -1.012238
                else:
                    var222 = 0.35106203
            else:
                if input[8] < 96.0:
                    var222 = -2.0938838
                else:
                    var222 = -0.13296966
        else:
            if input[1] < 320.0:
                if input[2] < 17.43:
                    var222 = -0.061777443
                else:
                    var222 = 1.380587
            else:
                if input[1] < 1077.0:
                    var222 = -0.9531545
                else:
                    var222 = 0.65892524
    else:
        if input[4] < 66.496155:
            if input[1] < 965.0:
                if input[1] < 368.0:
                    var222 = 0.19682853
                else:
                    var222 = 1.4173695
            else:
                if input[3] < 121.0:
                    var222 = -2.2232141
                else:
                    var222 = -0.0548055
        else:
            if input[4] < 66.75667:
                if input[1] < 104.0:
                    var222 = 0.35913086
                else:
                    var222 = -3.477237
            else:
                if input[3] < 2.5:
                    var222 = -1.1301564
                else:
                    var222 = 0.035856057
    if input[2] < 171.32:
        if input[0] < 14.0:
            if input[0] < 5.0:
                if input[1] < 89.0:
                    var223 = -0.6827206
                else:
                    var223 = 0.24088739
            else:
                if input[8] < 49.0:
                    var223 = -2.083764
                else:
                    var223 = -0.19383918
        else:
            var223 = 2.7839112
    else:
        if input[2] < 193.05:
            if input[1] < 893.0:
                var223 = 3.4120796
            else:
                var223 = 0.31326753
        else:
            if input[1] < 1158.0:
                if input[1] < 1136.0:
                    var223 = 0.027876532
                else:
                    var223 = 1.5672791
            else:
                if input[1] < 1185.0:
                    var223 = -1.1572968
                else:
                    var223 = 0.60125846
    if input[8] < 49.0:
        if input[4] < 125.935:
            if input[4] < 118.291664:
                if input[3] < 150.2:
                    var224 = -0.18789673
                else:
                    var224 = 1.0535583
            else:
                if input[0] < 12.0:
                    var224 = -3.4611866
                else:
                    var224 = 0.19829713
        else:
            if input[4] < 169.41692:
                if input[1] < 716.0:
                    var224 = 0.41663906
                else:
                    var224 = 2.7712724
            else:
                if input[8] < 44.0:
                    var224 = 0.049216468
                else:
                    var224 = 1.5223619
    else:
        if input[8] < 50.0:
            if input[2] < 568.58:
                if input[2] < 407.43:
                    var224 = 2.130791
                else:
                    var224 = -1.3934324
            else:
                if input[2] < 716.7:
                    var224 = -2.7892106
                else:
                    var224 = -8.200484
        else:
            if input[8] < 58.0:
                if input[2] < 540.6:
                    var224 = -0.67783
                else:
                    var224 = 1.068967
            else:
                if input[8] < 62.0:
                    var224 = -0.92730635
                else:
                    var224 = 0.073289216
    if input[7] < 14.0:
        if input[4] < 396.49:
            if input[4] < 375.698:
                if input[4] < 356.10333:
                    var225 = -0.02641789
                else:
                    var225 = 1.7415879
            else:
                if input[1] < 389.0:
                    var225 = 1.1782776
                else:
                    var225 = -3.8997364
        else:
            if input[1] < 432.0:
                if input[4] < 758.27:
                    var225 = 0.20796981
                else:
                    var225 = -0.67934674
            else:
                if input[3] < 181.0:
                    var225 = 2.290014
                else:
                    var225 = 0.5179422
    else:
        if input[7] < 19.0:
            if input[2] < 202.49:
                var225 = 1.2815659
            else:
                if input[3] < 388.0:
                    var225 = -1.9628356
                else:
                    var225 = -0.68184394
        else:
            if input[6] < 34.0:
                if input[1] < 1046.0:
                    var225 = -0.6745604
                else:
                    var225 = 0.7240357
            else:
                if input[9] < 71.0:
                    var225 = 1.6541351
                else:
                    var225 = 0.37024298
    if input[1] < 532.0:
        if input[4] < 492.1575:
            if input[4] < 133.09222:
                if input[4] < 66.496155:
                    var226 = 0.339591
                else:
                    var226 = -0.60333073
            else:
                if input[1] < 483.0:
                    var226 = 0.42289206
                else:
                    var226 = 1.7349201
        else:
            if input[2] < 2328.11:
                if input[8] < 23.0:
                    var226 = 0.053763874
                else:
                    var226 = -1.213968
            else:
                if input[7] < 5.0:
                    var226 = 0.9818395
                else:
                    var226 = -0.73934937
    else:
        if input[8] < 27.0:
            if input[1] < 934.0:
                if input[8] < 10.0:
                    var226 = -0.105614044
                else:
                    var226 = -1.581638
            else:
                if input[2] < 664.9:
                    var226 = 1.3262002
                else:
                    var226 = -0.44530255
        else:
            if input[7] < 4.0:
                if input[8] < 71.0:
                    var226 = -1.0994208
                else:
                    var226 = 0.14893875
            else:
                if input[8] < 76.0:
                    var226 = 0.56956255
                else:
                    var226 = -0.3862539
    if input[2] < 2419.86:
        if input[8] < 49.0:
            if input[2] < 1171.99:
                if input[4] < 82.643074:
                    var227 = 0.3412482
                else:
                    var227 = -0.37362167
            else:
                if input[2] < 1191.4:
                    var227 = 3.9184632
                else:
                    var227 = 0.3573917
        else:
            if input[8] < 50.0:
                if input[2] < 497.7:
                    var227 = 0.91027784
                else:
                    var227 = -6.353537
            else:
                if input[4] < 24.540909:
                    var227 = 0.582607
                else:
                    var227 = -0.06959988
    else:
        if input[1] < 463.0:
            if input[1] < 173.0:
                if input[2] < 2462.26:
                    var227 = -1.3287672
                else:
                    var227 = 1.2417786
            else:
                if input[0] < 10.0:
                    var227 = 1.8103923
                else:
                    var227 = 0.3834717
        else:
            if input[1] < 793.0:
                if input[0] < 8.0:
                    var227 = -0.6247823
                else:
                    var227 = -2.7899415
            else:
                if input[8] < 30.0:
                    var227 = 0.11559693
                else:
                    var227 = -1.1593026
    if input[4] < 258.2443:
        if input[4] < 245.9425:
            if input[8] < 92.0:
                if input[8] < 90.0:
                    var228 = 0.13124792
                else:
                    var228 = 1.6223958
            else:
                if input[4] < 8.236:
                    var228 = 1.6373032
                else:
                    var228 = -0.67723274
        else:
            if input[2] < 2235.72:
                if input[0] < 3.0:
                    var228 = -0.68757
                else:
                    var228 = 2.7805755
            else:
                var228 = -2.1866548
    else:
        if input[0] < 8.0:
            if input[8] < 50.0:
                if input[8] < 49.0:
                    var228 = -0.06315881
                else:
                    var228 = -4.6996875
            else:
                if input[4] < 616.0725:
                    var228 = 0.52223444
                else:
                    var228 = -0.22110386
        else:
            if input[1] < 527.0:
                if input[1] < 278.0:
                    var228 = -1.4727677
                else:
                    var228 = 0.6543762
            else:
                if input[8] < 34.0:
                    var228 = -3.037256
                else:
                    var228 = -1.3350174
    if input[8] < 1.0:
        if input[4] < 194.44112:
            if input[0] < 4.0:
                var229 = 0.51793975
            else:
                var229 = 1.9247726
        else:
            if input[0] < 2.0:
                var229 = -0.21793823
            else:
                var229 = 0.12140198
    else:
        if input[4] < 39.6625:
            if input[4] < 22.4975:
                if input[8] < 94.0:
                    var229 = -0.09272228
                else:
                    var229 = 1.2784364
            else:
                if input[6] < 10.0:
                    var229 = -1.3396145
                else:
                    var229 = 1.8545685
        else:
            if input[4] < 47.13:
                if input[1] < 710.0:
                    var229 = 1.3787671
                else:
                    var229 = -0.6894361
            else:
                if input[8] < 50.0:
                    var229 = -0.16523032
                else:
                    var229 = 0.10979692
    if input[1] < 774.0:
        if input[1] < 763.0:
            if input[4] < 131.048:
                if input[6] < 18.0:
                    var230 = 0.17048967
                else:
                    var230 = -0.9816419
            else:
                if input[4] < 140.93857:
                    var230 = 1.5908917
                else:
                    var230 = 0.14701112
        else:
            if input[8] < 76.0:
                if input[2] < 880.17:
                    var230 = 0.5978058
                else:
                    var230 = -1.9406708
            else:
                var230 = 3.3530254
    else:
        if input[3] < 78.75:
            if input[8] < 46.0:
                if input[3] < 57.642857:
                    var230 = 0.605954
                else:
                    var230 = -2.2580845
            else:
                if input[8] < 49.0:
                    var230 = 3.8439515
                else:
                    var230 = -0.81240386
        else:
            if input[2] < 2359.42:
                if input[3] < 83.916664:
                    var230 = 1.0811743
                else:
                    var230 = -0.035591405
            else:
                if input[1] < 1086.0:
                    var230 = -1.3446727
                else:
                    var230 = 0.05718079
    if input[1] < 896.0:
        if input[1] < 888.0:
            if input[8] < 99.0:
                if input[2] < 2489.69:
                    var231 = 0.08151719
                else:
                    var231 = 1.3835896
            else:
                if input[3] < 34.6:
                    var231 = -2.4948924
                else:
                    var231 = -0.32973862
        else:
            if input[8] < 73.0:
                if input[1] < 893.0:
                    var231 = 2.6593482
                else:
                    var231 = 0.1445816
            else:
                if input[0] < 2.0:
                    var231 = -0.13622132
                else:
                    var231 = -0.6532837
    else:
        if input[4] < 1927.75:
            if input[2] < 1241.21:
                if input[2] < 1147.89:
                    var231 = -0.22491887
                else:
                    var231 = 3.8869894
            else:
                if input[1] < 934.0:
                    var231 = -2.251105
                else:
                    var231 = -0.41014677
        else:
            if input[1] < 993.0:
                var231 = 0.5487183
            else:
                var231 = 2.3797953
    if input[1] < 904.0:
        if input[8] < 93.0:
            if input[8] < 90.0:
                if input[1] < 875.0:
                    var232 = 0.002146
                else:
                    var232 = 1.0815043
            else:
                if input[1] < 625.0:
                    var232 = 0.6194517
                else:
                    var232 = 2.6555197
        else:
            if input[4] < 8.236:
                if input[2] < 19.76:
                    var232 = -0.53948975
                else:
                    var232 = 1.2299846
            else:
                if input[4] < 241.62714:
                    var232 = -1.0255557
                else:
                    var232 = 0.16032785
    else:
        if input[1] < 941.0:
            if input[8] < 96.0:
                if input[0] < 11.0:
                    var232 = -1.0394175
                else:
                    var232 = -2.8953807
            else:
                if input[0] < 2.0:
                    var232 = 0.9586609
                else:
                    var232 = 0.11934509
        else:
            if input[4] < 66.75667:
                if input[2] < 631.88:
                    var232 = -0.55543363
                else:
                    var232 = -3.273405
            else:
                if input[4] < 169.41692:
                    var232 = 0.6491309
                else:
                    var232 = -0.2682491
    if input[3] < 44.11111:
        if input[2] < 2462.26:
            if input[4] < 231.4943:
                if input[1] < 173.0:
                    var233 = 0.18972151
                else:
                    var233 = -0.5097678
            else:
                if input[8] < 68.0:
                    var233 = -1.8587116
                else:
                    var233 = 0.34989563
        else:
            if input[8] < 23.0:
                var233 = -0.063510135
            else:
                var233 = 2.0868852
    else:
        if input[3] < 51.25:
            if input[0] < 11.0:
                if input[4] < 219.127:
                    var233 = -0.66756976
                else:
                    var233 = 1.0977265
            else:
                if input[3] < 47.909092:
                    var233 = 1.3640076
                else:
                    var233 = 3.714054
        else:
            if input[4] < 45.59:
                if input[6] < 3.0:
                    var233 = -0.03699529
                else:
                    var233 = -0.97738427
            else:
                if input[4] < 69.535:
                    var233 = 0.96811897
                else:
                    var233 = -0.029428322
    if input[3] < 250.0:
        if input[3] < 210.0:
            if input[3] < 151.0:
                if input[3] < 131.8:
                    var234 = -0.05464955
                else:
                    var234 = -0.69230825
            else:
                if input[2] < 438.96:
                    var234 = -0.8775692
                else:
                    var234 = 0.7006517
        else:
            if input[4] < 511.77:
                if input[1] < 1086.0:
                    var234 = -2.252281
                else:
                    var234 = -0.18868409
            else:
                if input[1] < 844.0:
                    var234 = -0.18746077
                else:
                    var234 = 1.9333466
    else:
        if input[3] < 261.75:
            if input[4] < 616.0725:
                var234 = 3.205016
            else:
                if input[4] < 726.05334:
                    var234 = -0.21113281
                else:
                    var234 = 1.2516632
        else:
            if input[4] < 115.82:
                if input[7] < 11.0:
                    var234 = -0.2790685
                else:
                    var234 = 1.4081037
            else:
                if input[4] < 396.49:
                    var234 = -0.5201521
                else:
                    var234 = 0.22380565
    if input[3] < 89.22222:
        if input[1] < 1145.0:
            if input[1] < 1056.0:
                if input[1] < 924.0:
                    var235 = 0.21435256
                else:
                    var235 = -0.6172886
            else:
                if input[2] < 1768.53:
                    var235 = 2.7807312
                else:
                    var235 = -0.64694214
        else:
            if input[1] < 1159.0:
                if input[2] < 347.82:
                    var235 = -0.8429657
                else:
                    var235 = -3.2260723
            else:
                var235 = -0.25834963
    else:
        if input[8] < 27.0:
            if input[3] < 154.0:
                if input[3] < 145.75:
                    var235 = -0.75088865
                else:
                    var235 = -2.8625734
            else:
                if input[0] < 5.0:
                    var235 = -0.29560536
                else:
                    var235 = 2.2503784
        else:
            if input[8] < 46.0:
                if input[1] < 1025.03:
                    var235 = 1.0056343
                else:
                    var235 = -0.5841985
            else:
                if input[8] < 50.0:
                    var235 = -1.487455
                else:
                    var235 = -0.051989228
    if input[3] < 70.25:
        if input[3] < 60.636364:
            if input[3] < 57.642857:
                if input[3] < 46.142857:
                    var236 = -0.037373774
                else:
                    var236 = 0.78732073
            else:
                if input[4] < 203.704:
                    var236 = -1.7641696
                else:
                    var236 = 0.17218934
        else:
            if input[1] < 770.0:
                if input[3] < 64.57143:
                    var236 = 1.897559
                else:
                    var236 = 0.22473243
            else:
                if input[1] < 868.0:
                    var236 = -1.5167184
                else:
                    var236 = 1.1177262
    else:
        if input[3] < 72.666664:
            if input[0] < 10.0:
                var236 = -2.8566473
            else:
                if input[0] < 13.0:
                    var236 = 1.0708649
                else:
                    var236 = -1.6579987
        else:
            if input[3] < 73.55556:
                if input[2] < 517.54:
                    var236 = -1.3602151
                else:
                    var236 = 3.899138
            else:
                if input[4] < 182.08:
                    var236 = -0.38838637
                else:
                    var236 = -0.037040737
    if input[1] < 1100.0:
        if input[1] < 1070.0:
            if input[1] < 1062.0:
                if input[2] < 2077.07:
                    var237 = -0.05946366
                else:
                    var237 = 0.30396816
            else:
                if input[2] < 2013.45:
                    var237 = 2.821875
                else:
                    var237 = -0.578949
        else:
            if input[0] < 10.0:
                if input[1] < 1086.0:
                    var237 = -2.4316347
                else:
                    var237 = -0.025791017
            else:
                if input[2] < 1072.44:
                    var237 = 1.1180512
                else:
                    var237 = -0.31944093
    else:
        if input[1] < 1116.0:
            if input[8] < 30.0:
                if input[0] < 4.0:
                    var237 = -0.49211884
                else:
                    var237 = 0.46340027
            else:
                if input[2] < 545.84:
                    var237 = 0.9037517
                else:
                    var237 = 3.1034744
        else:
            if input[4] < 208.32:
                if input[8] < 62.0:
                    var237 = 0.0821669
                else:
                    var237 = 1.498868
            else:
                if input[1] < 1182.0:
                    var237 = -0.9300168
                else:
                    var237 = 1.2852852
    if input[1] < 1162.0:
        if input[1] < 1145.0:
            if input[2] < 1742.62:
                if input[3] < 145.75:
                    var238 = 0.18526606
                else:
                    var238 = -0.27090147
            else:
                if input[4] < 448.32:
                    var238 = -0.4714354
                else:
                    var238 = 0.2160089
        else:
            if input[2] < 2218.74:
                if input[8] < 44.0:
                    var238 = 0.33615926
                else:
                    var238 = -2.3144472
            else:
                var238 = 1.2091817
    else:
        if input[1] < 1187.0:
            if input[2] < 1871.77:
                var238 = 2.3331048
            else:
                if input[2] < 2273.6:
                    var238 = -0.90369266
                else:
                    var238 = 0.1809896
        else:
            if input[2] < 1639.17:
                if input[3] < 399.0:
                    var238 = -1.7947361
                else:
                    var238 = 1.6554902
            else:
                if input[3] < 199.66667:
                    var238 = 0.58813274
                else:
                    var238 = 2.5160034
    var239 = var183 + var184 + var185 + var186 + var187 + var188 + var189 + var190 + var191 + var192 + var193 + var194 + var195 + var196 + var197 + var198 + var199 + var200 + var201 + var202 + var203 + var204 + var205 + var206 + var207 + var208 + var209 + var210 + var211 + var212 + var213 + var214 + var215 + var216 + var217 + var218 + var219 + var220 + var221 + var222 + var223 + var224 + var225 + var226 + var227 + var228 + var229 + var230 + var231 + var232 + var233 + var234 + var235 + var236 + var237 + var238
    if input[3] < 491.5:
        if input[7] < 14.0:
            if input[3] < 252.75:
                if input[8] < 45.0:
                    var240 = 0.10311514
                else:
                    var240 = -0.18101504
            else:
                if input[3] < 261.75:
                    var240 = 1.9828844
                else:
                    var240 = 0.31416258
        else:
            if input[1] < 1139.0:
                if input[3] < 399.0:
                    var240 = -0.0091435155
                else:
                    var240 = -0.9422439
            else:
                var240 = -1.7791194
    else:
        if input[3] < 673.0:
            if input[4] < 923.0:
                if input[1] < 534.0:
                    var240 = -0.004751587
                else:
                    var240 = 2.0786116
            else:
                if input[0] < 2.0:
                    var240 = -0.23773602
                else:
                    var240 = 0.36626586
        else:
            if input[8] < 48.0:
                if input[1] < 795.0:
                    var240 = -0.3515503
                else:
                    var240 = 1.4040202
            else:
                if input[8] < 54.0:
                    var240 = -1.4660485
                else:
                    var240 = 0.01951163
    if input[3] < 188.4:
        if input[7] < 4.0:
            if input[3] < 95.4:
                if input[0] < 7.0:
                    var241 = 0.4452183
                else:
                    var241 = -0.05274352
            else:
                if input[0] < 11.0:
                    var241 = -1.7737955
                else:
                    var241 = 1.1621379
        else:
            if input[3] < 106.25:
                if input[2] < 314.81:
                    var241 = -1.130205
                else:
                    var241 = 2.32598
            else:
                if input[3] < 142.5:
                    var241 = -0.23504463
                else:
                    var241 = 0.60845757
    else:
        if input[0] < 5.0:
            if input[4] < 115.82:
                if input[8] < 63.0:
                    var241 = 1.5034754
                else:
                    var241 = -0.514622
            else:
                if input[8] < 58.0:
                    var241 = -0.36242768
                else:
                    var241 = 0.42107853
        else:
            if input[1] < 1199.0:
                if input[8] < 20.0:
                    var241 = 0.63135684
                else:
                    var241 = -1.8613539
            else:
                var241 = 2.0490632
    if input[8] < 4.0:
        if input[0] < 10.0:
            if input[4] < 349.68857:
                if input[2] < 709.07:
                    var242 = 0.20213433
                else:
                    var242 = 2.1065903
            else:
                if input[0] < 2.0:
                    var242 = 0.15180436
                else:
                    var242 = -1.1954163
        else:
            if input[2] < 497.7:
                var242 = 1.4810567
            else:
                if input[3] < 5.7:
                    var242 = 0.4512085
                else:
                    var242 = -0.9572304
    else:
        if input[5] < 7.0:
            if input[4] < 758.27:
                if input[3] < 44.5:
                    var242 = -0.3709229
                else:
                    var242 = 0.24217384
            else:
                if input[3] < 311.0:
                    var242 = -1.0102276
                else:
                    var242 = 0.30011597
        else:
            if input[3] < 67.36364:
                if input[3] < 60.636364:
                    var242 = 0.027169703
                else:
                    var242 = 1.4892994
            else:
                if input[8] < 32.0:
                    var242 = -0.4864593
                else:
                    var242 = 0.1087868
    if input[1] < 597.0:
        if input[1] < 560.0:
            if input[8] < 32.0:
                if input[1] < 483.0:
                    var243 = 0.022015836
                else:
                    var243 = 2.4335315
            else:
                if input[8] < 50.0:
                    var243 = -0.69377524
                else:
                    var243 = -0.052881837
        else:
            if input[4] < 173.92125:
                if input[0] < 14.0:
                    var243 = -2.6657827
                else:
                    var243 = 0.48542482
            else:
                if input[8] < 16.0:
                    var243 = -0.9098694
                else:
                    var243 = 0.9809125
    else:
        if input[3] < 51.25:
            if input[3] < 47.2:
                if input[1] < 620.0:
                    var243 = -0.8237366
                else:
                    var243 = 0.9944672
            else:
                var243 = 3.7699819
        else:
            if input[3] < 62.0:
                if input[2] < 2195.67:
                    var243 = -1.2796171
                else:
                    var243 = 0.4314654
            else:
                if input[3] < 67.36364:
                    var243 = 1.7640905
                else:
                    var243 = 0.06735989
    if input[2] < 2419.86:
        if input[7] < 14.0:
            if input[4] < 758.27:
                if input[4] < 562.6275:
                    var244 = 0.10899176
                else:
                    var244 = 1.1365999
            else:
                if input[3] < 311.0:
                    var244 = -1.0336081
                else:
                    var244 = 0.7527118
        else:
            if input[7] < 19.0:
                if input[1] < 934.0:
                    var244 = -0.7479645
                else:
                    var244 = -1.9460754
            else:
                if input[1] < 1109.0:
                    var244 = -0.08805145
                else:
                    var244 = 1.4231524
    else:
        if input[0] < 7.0:
            if input[2] < 2489.69:
                if input[1] < 89.0:
                    var244 = 1.1367553
                else:
                    var244 = -0.54069215
            else:
                var244 = 2.1147249
        else:
            if input[3] < 21.571428:
                if input[1] < 112.0:
                    var244 = -0.8362012
                else:
                    var244 = 1.2296855
            else:
                if input[0] < 13.0:
                    var244 = -2.526009
                else:
                    var244 = -0.18631744
    if input[4] < 93.88143:
        if input[3] < 108.375:
            if input[4] < 86.75:
                if input[2] < 1129.52:
                    var245 = -0.030234415
                else:
                    var245 = 3.6159484
            else:
                if input[3] < 66.666664:
                    var245 = -1.1562654
                else:
                    var245 = 0.47250184
        else:
            if input[0] < 5.0:
                if input[2] < 202.49:
                    var245 = 0.51264584
                else:
                    var245 = -2.0740876
            else:
                if input[8] < 41.0:
                    var245 = -2.6195672
                else:
                    var245 = -0.31321123
    else:
        if input[4] < 95.216:
            var245 = 4.385744
        else:
            if input[8] < 91.0:
                if input[8] < 78.0:
                    var245 = 0.063197315
                else:
                    var245 = 0.597021
            else:
                if input[4] < 239.245:
                    var245 = -1.1890138
                else:
                    var245 = 0.28107128
    if input[8] < 4.0:
        if input[4] < 349.68857:
            if input[0] < 8.0:
                if input[4] < 187.2825:
                    var246 = 0.7432146
                else:
                    var246 = 2.4221053
            else:
                if input[3] < 92.666664:
                    var246 = 0.2888141
                else:
                    var246 = -1.162378
        else:
            if input[0] < 2.0:
                if input[1] < 218.0:
                    var246 = 0.37519607
                else:
                    var246 = -0.08515828
            else:
                var246 = -1.1627991
    else:
        if input[1] < 1145.0:
            if input[1] < 1086.0:
                if input[1] < 893.0:
                    var246 = -0.001984885
                else:
                    var246 = -0.39633045
            else:
                if input[4] < 205.0089:
                    var246 = 1.5730308
                else:
                    var246 = -0.1362667
        else:
            if input[2] < 1114.96:
                if input[8] < 92.0:
                    var246 = -1.9329424
                else:
                    var246 = 1.8859619
            else:
                if input[1] < 1192.0:
                    var246 = -0.12075501
                else:
                    var246 = 1.6715927
    if input[8] < 99.0:
        if input[2] < 2462.26:
            if input[6] < 49.0:
                if input[4] < 1143.58:
                    var247 = 0.10935527
                else:
                    var247 = -0.35728645
            else:
                if input[8] < 54.0:
                    var247 = -0.41748658
                else:
                    var247 = -1.5282319
        else:
            if input[1] < 403.0:
                var247 = 2.2456117
            else:
                if input[1] < 532.0:
                    var247 = -1.4004425
                else:
                    var247 = 0.26928848
    else:
        if input[3] < 34.6:
            var247 = -2.3450859
        else:
            if input[1] < 725.0:
                if input[3] < 66.666664:
                    var247 = 0.6815069
                else:
                    var247 = -0.16753025
            else:
                if input[0] < 5.0:
                    var247 = 0.072416686
                else:
                    var247 = -1.5700755
    if input[0] < 8.0:
        if input[8] < 82.0:
            if input[9] < 15.0:
                if input[2] < 709.07:
                    var248 = 0.025636572
                else:
                    var248 = 0.81443757
            else:
                if input[3] < 491.5:
                    var248 = -0.3509639
                else:
                    var248 = 0.5843874
        else:
            if input[9] < 11.0:
                if input[2] < 651.64:
                    var248 = -0.43335292
                else:
                    var248 = -1.9189644
            else:
                if input[1] < 255.0:
                    var248 = -1.2015051
                else:
                    var248 = 0.3159959
    else:
        if input[9] < 9.0:
            if input[7] < 4.0:
                if input[3] < 83.916664:
                    var248 = -0.020060537
                else:
                    var248 = -0.9498742
            else:
                if input[8] < 32.0:
                    var248 = -2.1884024
                else:
                    var248 = 1.5032557
        else:
            if input[1] < 467.0:
                if input[2] < 2265.21:
                    var248 = -0.8712657
                else:
                    var248 = 1.7949717
            else:
                if input[1] < 1100.0:
                    var248 = -2.369188
                else:
                    var248 = -0.30633852
    if input[3] < 470.5:
        if input[4] < 1191.195:
            if input[1] < 904.0:
                if input[1] < 875.0:
                    var249 = 0.049113784
                else:
                    var249 = 1.4012245
            else:
                if input[5] < 20.0:
                    var249 = -0.8775453
                else:
                    var249 = -0.009099977
        else:
            if input[1] < 19.0:
                var249 = 1.0492676
            else:
                if input[1] < 45.0:
                    var249 = -0.21400757
                else:
                    var249 = -1.5986285
    else:
        if input[3] < 673.0:
            if input[8] < 75.0:
                if input[8] < 19.0:
                    var249 = 0.09091797
                else:
                    var249 = 1.9772552
            else:
                if input[1] < 534.0:
                    var249 = -0.025045013
                else:
                    var249 = 0.51601565
        else:
            if input[2] < 1815.6:
                if input[8] < 85.0:
                    var249 = -0.4211977
                else:
                    var249 = 0.91345596
            else:
                if input[2] < 2152.66:
                    var249 = 2.1238022
                else:
                    var249 = 0.874231
    if input[7] < 19.0:
        if input[4] < 1191.195:
            if input[2] < 39.86:
                if input[1] < 59.0:
                    var250 = -0.5113319
                else:
                    var250 = 0.91982204
            else:
                if input[2] < 47.46:
                    var250 = -1.7293304
                else:
                    var250 = -0.06050799
        else:
            if input[1] < 45.0:
                if input[0] < 2.0:
                    var250 = -0.18918051
                else:
                    var250 = 1.0230347
            else:
                if input[8] < 66.0:
                    var250 = -1.6151909
                else:
                    var250 = -0.65216064
    else:
        if input[3] < 673.0:
            if input[8] < 12.0:
                if input[0] < 2.0:
                    var250 = -0.19101258
                else:
                    var250 = -1.5988343
            else:
                if input[4] < 935.78:
                    var250 = 1.8623326
                else:
                    var250 = 0.49666595
        else:
            if input[2] < 1300.05:
                if input[8] < 85.0:
                    var250 = -0.85238916
                else:
                    var250 = 0.8968369
            else:
                if input[1] < 684.0:
                    var250 = -0.55009973
                else:
                    var250 = 0.7768561
    if input[0] < 10.0:
        if input[0] < 8.0:
            if input[8] < 10.0:
                if input[0] < 5.0:
                    var251 = -0.103924036
                else:
                    var251 = 1.3160927
            else:
                if input[8] < 16.0:
                    var251 = -1.0795417
                else:
                    var251 = 0.008097137
        else:
            if input[4] < 155.39333:
                if input[8] < 32.0:
                    var251 = -1.3936266
                else:
                    var251 = 0.352023
            else:
                if input[3] < 59.0:
                    var251 = 0.06886231
                else:
                    var251 = -1.6890754
    else:
        if input[3] < 99.545456:
            if input[8] < 90.0:
                if input[8] < 30.0:
                    var251 = 0.58888286
                else:
                    var251 = -0.22214726
            else:
                if input[8] < 92.0:
                    var251 = 2.8198562
                else:
                    var251 = 0.19828175
        else:
            if input[4] < 25.788:
                var251 = -1.2910584
            else:
                if input[8] < 37.0:
                    var251 = 0.15305421
                else:
                    var251 = 3.0644298
    if input[8] < 27.0:
        if input[1] < 522.0:
            if input[1] < 483.0:
                if input[1] < 447.0:
                    var252 = 0.20917182
                else:
                    var252 = -1.4706604
            else:
                if input[2] < 1957.9:
                    var252 = 3.1163566
                else:
                    var252 = 0.14976807
        else:
            if input[4] < 216.87273:
                if input[2] < 171.32:
                    var252 = -2.0634165
                else:
                    var252 = -0.12425988
            else:
                if input[4] < 344.00287:
                    var252 = -2.4561098
                else:
                    var252 = -0.29017362
    else:
        if input[8] < 30.0:
            if input[4] < 153.15:
                if input[1] < 459.0:
                    var252 = 0.6145162
                else:
                    var252 = 3.4021893
            else:
                if input[2] < 1901.83:
                    var252 = -1.2123405
                else:
                    var252 = 1.4851557
        else:
            if input[1] < 259.96:
                if input[0] < 14.0:
                    var252 = -0.28485534
                else:
                    var252 = 1.0117058
            else:
                if input[2] < 2367.63:
                    var252 = 0.24151866
                else:
                    var252 = -0.53556323
    if input[0] < 10.0:
        if input[7] < 19.0:
            if input[8] < 2.0:
                if input[0] < 5.0:
                    var253 = 0.42450675
                else:
                    var253 = 1.9004242
            else:
                if input[2] < 23.47:
                    var253 = 0.7510159
                else:
                    var253 = -0.17706849
        else:
            if input[4] < 369.13333:
                if input[2] < 330.29:
                    var253 = 0.21484272
                else:
                    var253 = -1.7172215
            else:
                if input[7] < 26.0:
                    var253 = 1.6315044
                else:
                    var253 = 0.38600394
    else:
        if input[1] < 1020.0:
            if input[1] < 924.0:
                if input[1] < 482.0:
                    var253 = 0.0340234
                else:
                    var253 = 0.53807753
            else:
                if input[1] < 934.0:
                    var253 = -3.1649978
                else:
                    var253 = -0.5179236
        else:
            if input[2] < 517.54:
                if input[0] < 14.0:
                    var253 = 0.40052423
                else:
                    var253 = -3.0796897
            else:
                if input[4] < 85.848:
                    var253 = 4.13318
                else:
                    var253 = 0.75034183
    if input[0] < 10.0:
        if input[0] < 8.0:
            if input[0] < 7.0:
                if input[3] < 101.28571:
                    var254 = 0.1906192
                else:
                    var254 = -0.21143706
            else:
                if input[3] < 44.5:
                    var254 = -1.230286
                else:
                    var254 = 0.9929454
        else:
            if input[2] < 1947.68:
                if input[3] < 100.6:
                    var254 = -0.7305952
                else:
                    var254 = 0.5887089
            else:
                if input[3] < 59.0:
                    var254 = -0.1260759
                else:
                    var254 = -2.6331732
    else:
        if input[3] < 99.545456:
            if input[8] < 30.0:
                if input[4] < 182.08:
                    var254 = 0.94132966
                else:
                    var254 = -0.8579961
            else:
                if input[8] < 47.0:
                    var254 = -0.99077225
                else:
                    var254 = 0.22161005
        else:
            if input[3] < 107.57143:
                if input[4] < 205.0089:
                    var254 = 2.8196805
                else:
                    var254 = 0.60546875
            else:
                var254 = -0.659372
    if input[1] < 333.0:
        if input[8] < 17.0:
            if input[3] < 2.5:
                if input[1] < 11.0:
                    var255 = -1.4120564
                else:
                    var255 = -0.467808
            else:
                if input[4] < 32.035:
                    var255 = 1.3374561
                else:
                    var255 = 0.16479886
        else:
            if input[8] < 77.0:
                if input[1] < 286.0:
                    var255 = -0.35051987
                else:
                    var255 = -1.4640334
            else:
                if input[8] < 84.0:
                    var255 = 1.0616692
                else:
                    var255 = -0.3132911
    else:
        if input[3] < 55.0:
            if input[4] < 43.54625:
                if input[1] < 384.0:
                    var255 = -0.8095345
                else:
                    var255 = 3.7686284
            else:
                if input[2] < 1227.21:
                    var255 = -0.80767584
                else:
                    var255 = 0.7776105
        else:
            if input[4] < 45.59:
                if input[2] < 39.86:
                    var255 = 1.0654907
                else:
                    var255 = -1.0154476
            else:
                if input[3] < 60.636364:
                    var255 = -0.8996231
                else:
                    var255 = 0.11737905
    if input[8] < 49.0:
        if input[0] < 10.0:
            if input[3] < 215.4:
                if input[8] < 33.0:
                    var256 = 0.21028279
                else:
                    var256 = 0.81706524
            else:
                if input[3] < 815.0:
                    var256 = -0.37280482
                else:
                    var256 = 1.2590545
        else:
            if input[8] < 48.0:
                if input[8] < 31.0:
                    var256 = 0.16658445
                else:
                    var256 = -0.9656553
            else:
                if input[0] < 12.0:
                    var256 = -0.64973754
                else:
                    var256 = 4.252881
    else:
        if input[8] < 50.0:
            if input[6] < 12.0:
                if input[1] < 265.0:
                    var256 = 2.4382613
                else:
                    var256 = -0.61440414
            else:
                if input[4] < 378.305:
                    var256 = -8.144528
                else:
                    var256 = -2.6144004
        else:
            if input[4] < 206.61363:
                if input[3] < 116.71429:
                    var256 = -0.12926674
                else:
                    var256 = -0.8078273
            else:
                if input[4] < 616.0725:
                    var256 = 0.39904094
                else:
                    var256 = -0.41406012
    if input[4] < 28.927143:
        if input[2] < 23.47:
            if input[1] < 66.13:
                if input[0] < 3.0:
                    var257 = -0.6847756
                else:
                    var257 = 0.14463043
            else:
                if input[8] < 76.0:
                    var257 = 0.98402673
                else:
                    var257 = -0.306707
        else:
            if input[1] < 793.0:
                if input[1] < 725.0:
                    var257 = -0.63972795
                else:
                    var257 = -2.4479835
            else:
                if input[1] < 1080.0:
                    var257 = 1.0143186
                else:
                    var257 = -1.5982527
    else:
        if input[1] < 1136.0:
            if input[1] < 1029.0:
                if input[1] < 1020.0:
                    var257 = -0.02717487
                else:
                    var257 = 1.9790366
            else:
                if input[0] < 11.0:
                    var257 = -0.88970345
                else:
                    var257 = 0.7768148
        else:
            if input[4] < 97.79667:
                var257 = 2.6486397
            else:
                if input[8] < 8.0:
                    var257 = -2.3981843
                else:
                    var257 = 0.24598746
    if input[0] < 8.0:
        if input[2] < 1690.22:
            if input[1] < 815.0:
                if input[1] < 751.0:
                    var258 = -0.05491957
                else:
                    var258 = 1.4234827
            else:
                if input[0] < 7.0:
                    var258 = -0.72189426
                else:
                    var258 = 0.86265296
        else:
            if input[4] < 254.578:
                var258 = 3.1998887
            else:
                if input[1] < 259.96:
                    var258 = -0.5528366
                else:
                    var258 = 0.57189924
    else:
        if input[4] < 150.28334:
            if input[2] < 1191.4:
                if input[2] < 927.74:
                    var258 = 0.10844608
                else:
                    var258 = -0.7648209
            else:
                if input[2] < 1429.04:
                    var258 = 1.4877572
                else:
                    var258 = 0.008718577
        else:
            if input[4] < 176.572:
                if input[8] < 40.0:
                    var258 = -0.19717689
                else:
                    var258 = -1.8582518
            else:
                if input[4] < 219.127:
                    var258 = 0.041227672
                else:
                    var258 = -1.0116473
    if input[3] < 9.375:
        if input[1] < 17.0:
            if input[8] < 71.0:
                if input[3] < 3.5:
                    var259 = -1.5585437
                else:
                    var259 = -0.2837087
            else:
                var259 = 1.5107392
        else:
            if input[3] < 8.2:
                if input[2] < 863.93:
                    var259 = 1.5468367
                else:
                    var259 = 0.067500815
            else:
                if input[2] < 507.59:
                    var259 = 0.15218964
                else:
                    var259 = 2.31937
    else:
        if input[4] < 93.88143:
            if input[2] < 927.74:
                if input[2] < 865.92:
                    var259 = -0.30488753
                else:
                    var259 = 1.8286704
            else:
                if input[2] < 950.23:
                    var259 = -3.1821618
                else:
                    var259 = -0.67408794
        else:
            if input[4] < 95.216:
                var259 = 3.974727
            else:
                if input[1] < 836.0:
                    var259 = 0.1106498
                else:
                    var259 = -0.19287714
    if input[8] < 49.0:
        if input[1] < 532.0:
            if input[1] < 482.0:
                if input[2] < 1820.8:
                    var260 = -0.0426078
                else:
                    var260 = 0.8094506
            else:
                if input[8] < 30.0:
                    var260 = 2.4582188
                else:
                    var260 = 0.1499231
        else:
            if input[1] < 586.0:
                if input[0] < 4.0:
                    var260 = -0.08554993
                else:
                    var260 = -2.7375424
            else:
                if input[8] < 48.0:
                    var260 = -0.09900166
                else:
                    var260 = 2.0166335
    else:
        if input[8] < 50.0:
            if input[2] < 568.58:
                if input[0] < 4.0:
                    var260 = -0.28063115
                else:
                    var260 = 2.7816691
            else:
                if input[0] < 5.0:
                    var260 = -3.3858392
                else:
                    var260 = -8.392629
        else:
            if input[8] < 60.0:
                if input[2] < 540.6:
                    var260 = -0.4873417
                else:
                    var260 = 0.6908494
            else:
                if input[4] < 21.13:
                    var260 = 0.49124295
                else:
                    var260 = -0.22413765
    if input[0] < 10.0:
        if input[4] < 193.4:
            if input[8] < 32.0:
                if input[1] < 1100.0:
                    var261 = -0.5800435
                else:
                    var261 = -2.8425903
            else:
                if input[8] < 46.0:
                    var261 = 1.0983542
                else:
                    var261 = -0.35963166
        else:
            if input[4] < 252.57286:
                if input[4] < 239.245:
                    var261 = 0.2625343
                else:
                    var261 = 2.5901499
            else:
                if input[0] < 8.0:
                    var261 = 0.019813519
                else:
                    var261 = -0.9292397
    else:
        if input[8] < 30.0:
            if input[4] < 182.08:
                if input[1] < 470.0:
                    var261 = 0.2987836
                else:
                    var261 = 1.5492967
            else:
                if input[7] < 4.0:
                    var261 = -0.70907813
                else:
                    var261 = 1.1719707
        else:
            if input[8] < 39.0:
                if input[7] < 2.0:
                    var261 = -0.06893311
                else:
                    var261 = -2.2444932
            else:
                if input[7] < 4.0:
                    var261 = 0.17328154
                else:
                    var261 = 1.6415192
    if input[1] < 94.0:
        if input[3] < 45.090908:
            if input[8] < 61.0:
                if input[8] < 29.0:
                    var262 = -0.026294274
                else:
                    var262 = -1.0158852
            else:
                if input[0] < 13.0:
                    var262 = 0.3614249
                else:
                    var262 = -0.96614075
        else:
            if input[0] < 2.0:
                var262 = -0.74123853
            else:
                var262 = -2.3161316
    else:
        if input[1] < 98.0:
            var262 = 2.5531938
        else:
            if input[8] < 76.0:
                if input[2] < 2265.21:
                    var262 = 0.01785523
                else:
                    var262 = 0.67543477
            else:
                if input[1] < 1162.0:
                    var262 = -0.258414
                else:
                    var262 = 1.7168127
    if input[0] < 8.0:
        if input[2] < 2328.11:
            if input[8] < 80.0:
                if input[4] < 263.01334:
                    var263 = 0.43620324
                else:
                    var263 = -0.20589368
            else:
                if input[4] < 181.24667:
                    var263 = -1.1365356
                else:
                    var263 = 0.21618621
        else:
            if input[0] < 4.0:
                if input[2] < 2440.91:
                    var263 = -0.6262118
                else:
                    var263 = 1.3066208
            else:
                if input[2] < 2385.6:
                    var263 = 2.2385204
                else:
                    var263 = 0.5131657
    else:
        if input[4] < 188.31:
            if input[9] < 5.0:
                if input[8] < 70.0:
                    var263 = -0.6254167
                else:
                    var263 = 0.4548533
            else:
                if input[3] < 103.2:
                    var263 = 0.21772759
                else:
                    var263 = 2.000349
        else:
            if input[8] < 55.0:
                if input[8] < 42.0:
                    var263 = -0.6722459
                else:
                    var263 = 1.2692578
            else:
                if input[5] < 23.0:
                    var263 = -1.3521672
                else:
                    var263 = 1.6509644
    if input[3] < 79.916664:
        if input[7] < 2.0:
            if input[8] < 28.0:
                if input[2] < 852.7:
                    var264 = 1.3874984
                else:
                    var264 = -0.024524307
            else:
                if input[3] < 33.81818:
                    var264 = -0.0081158355
                else:
                    var264 = -0.4916961
        else:
            if input[3] < 51.25:
                var264 = 3.5969772
            else:
                if input[0] < 8.0:
                    var264 = 0.8163148
                else:
                    var264 = 0.046197694
    else:
        if input[7] < 4.0:
            if input[2] < 1191.4:
                if input[2] < 950.23:
                    var264 = -0.26916027
                else:
                    var264 = 1.5253876
            else:
                if input[8] < 20.0:
                    var264 = 0.14149827
                else:
                    var264 = -1.5862817
        else:
            if input[3] < 103.2:
                if input[8] < 22.0:
                    var264 = -0.8106758
                else:
                    var264 = 2.2689667
            else:
                if input[4] < 87.72444:
                    var264 = -0.68241847
                else:
                    var264 = -0.022616778
    if input[4] < 356.10333:
        if input[1] < 1175.0:
            if input[3] < 131.8:
                if input[7] < 4.0:
                    var265 = -0.105129264
                else:
                    var265 = 0.47893235
            else:
                if input[3] < 141.0:
                    var265 = -1.3949914
                else:
                    var265 = -0.21797805
        else:
            if input[1] < 1187.0:
                if input[2] < 555.49:
                    var265 = 2.446631
                else:
                    var265 = 0.5722702
            else:
                if input[8] < 49.0:
                    var265 = 1.0087291
                else:
                    var265 = -0.6797814
    else:
        if input[0] < 4.0:
            if input[2] < 1072.44:
                if input[0] < 3.0:
                    var265 = 0.31417912
                else:
                    var265 = 2.2325237
            else:
                if input[2] < 1291.33:
                    var265 = -1.274845
                else:
                    var265 = -0.13183708
        else:
            if input[1] < 1012.0:
                if input[1] < 353.0:
                    var265 = 0.4422121
                else:
                    var265 = 2.2709694
            else:
                if input[4] < 511.77:
                    var265 = -1.1070917
                else:
                    var265 = 1.2692063
    if input[0] < 13.0:
        if input[2] < 2419.86:
            if input[6] < 42.0:
                if input[2] < 1516.42:
                    var266 = 0.0073622004
                else:
                    var266 = -0.35755917
            else:
                if input[4] < 181.24667:
                    var266 = 3.0567079
                else:
                    var266 = 0.21659417
        else:
            if input[1] < 463.0:
                if input[1] < 173.0:
                    var266 = -0.3459739
                else:
                    var266 = 1.9198288
            else:
                if input[3] < 221.5:
                    var266 = -1.5829271
                else:
                    var266 = 0.64795077
    else:
        if input[1] < 1145.0:
            if input[3] < 79.6:
                if input[3] < 55.0:
                    var266 = 0.6159752
                else:
                    var266 = -0.5301021
            else:
                if input[1] < 1056.0:
                    var266 = 0.7289368
                else:
                    var266 = 2.750122
        else:
            if input[2] < 497.7:
                if input[0] < 14.0:
                    var266 = 0.7125214
                else:
                    var266 = -0.53221434
            else:
                var266 = -3.0098045
    if input[8] < 53.0:
        if input[8] < 49.0:
            if input[4] < 93.88143:
                if input[4] < 81.93584:
                    var267 = -0.10851321
                else:
                    var267 = -1.55233
            else:
                if input[4] < 95.216:
                    var267 = 2.2691407
                else:
                    var267 = 0.07788669
        else:
            if input[8] < 50.0:
                if input[2] < 568.58:
                    var267 = 1.0565385
                else:
                    var267 = -6.0015287
            else:
                if input[4] < 162.135:
                    var267 = -1.3087502
                else:
                    var267 = 0.3417282
    else:
        if input[4] < 1143.58:
            if input[8] < 59.0:
                if input[4] < 173.92125:
                    var267 = -0.086921364
                else:
                    var267 = 1.265415
            else:
                if input[8] < 62.0:
                    var267 = -0.595906
                else:
                    var267 = 0.12917924
        else:
            if input[8] < 66.0:
                var267 = -1.4865854
            else:
                if input[1] < 1038.0:
                    var267 = -0.49474946
                else:
                    var267 = 0.6197733
    if input[8] < 76.0:
        if input[8] < 62.0:
            if input[2] < 1448.55:
                if input[4] < 216.87273:
                    var268 = 0.00029487134
                else:
                    var268 = -0.6976544
            else:
                if input[4] < 142.11667:
                    var268 = -0.7721619
                else:
                    var268 = 0.2932522
        else:
            if input[3] < 76.0:
                if input[3] < 47.2:
                    var268 = 0.019887954
                else:
                    var268 = 1.8807341
            else:
                if input[3] < 115.75:
                    var268 = -0.8417886
                else:
                    var268 = 0.6482976
    else:
        if input[1] < 831.0:
            if input[3] < 87.0:
                if input[3] < 46.142857:
                    var268 = 0.07261321
                else:
                    var268 = -0.8622123
            else:
                if input[2] < 1536.0:
                    var268 = 0.9560941
                else:
                    var268 = -0.29133606
        else:
            if input[0] < 9.0:
                if input[3] < 225.2:
                    var268 = -2.2473714
                else:
                    var268 = -0.4042143
            else:
                if input[8] < 80.0:
                    var268 = -0.9900214
                else:
                    var268 = 0.82769966
    if input[8] < 90.0:
        if input[3] < 131.8:
            if input[3] < 125.166664:
                if input[4] < 37.923077:
                    var269 = -0.3950436
                else:
                    var269 = 0.09063392
            else:
                if input[8] < 31.0:
                    var269 = 0.30751345
                else:
                    var269 = 2.6515365
        else:
            if input[3] < 150.2:
                if input[5] < 23.0:
                    var269 = -0.6530806
                else:
                    var269 = -2.331277
            else:
                if input[3] < 162.5:
                    var269 = 0.78984016
                else:
                    var269 = -0.17927419
    else:
        if input[8] < 92.0:
            if input[5] < 19.0:
                if input[3] < 47.909092:
                    var269 = 0.8493296
                else:
                    var269 = 3.4750905
            else:
                if input[2] < 672.91:
                    var269 = 0.24141847
                else:
                    var269 = -1.6270646
        else:
            if input[5] < 9.0:
                if input[4] < 8.236:
                    var269 = 1.5335919
                else:
                    var269 = -0.7760544
            else:
                if input[4] < 86.75:
                    var269 = 1.9890631
                else:
                    var269 = 0.07903433
    if input[1] < 697.0:
        if input[1] < 636.0:
            if input[1] < 597.0:
                if input[1] < 512.0:
                    var270 = 0.018414337
                else:
                    var270 = -0.71287215
            else:
                if input[4] < 21.13:
                    var270 = 3.2186666
                else:
                    var270 = 0.4278925
        else:
            if input[2] < 1279.51:
                if input[8] < 32.0:
                    var270 = -1.064798
                else:
                    var270 = -2.2561066
            else:
                if input[0] < 11.0:
                    var270 = -0.69421387
                else:
                    var270 = 0.6181664
    else:
        if input[1] < 710.0:
            if input[0] < 7.0:
                if input[1] < 708.0:
                    var270 = 0.93255615
                else:
                    var270 = 0.1815094
            else:
                var270 = 2.96183
        else:
            if input[3] < 62.0:
                if input[1] < 713.0:
                    var270 = 1.441917
                else:
                    var270 = -1.5768255
            else:
                if input[0] < 7.0:
                    var270 = -0.127856
                else:
                    var270 = 0.29731604
    if input[2] < 1358.14:
        if input[2] < 1346.21:
            if input[4] < 1143.58:
                if input[2] < 1143.58:
                    var271 = 0.09988101
                else:
                    var271 = 0.61750233
            else:
                if input[1] < 756.0:
                    var271 = -0.502861
                else:
                    var271 = -1.8463287
        else:
            if input[1] < 379.0:
                if input[1] < 273.0:
                    var271 = 0.39150697
                else:
                    var271 = -1.0342631
            else:
                var271 = 3.5767472
    else:
        if input[1] < 1185.0:
            if input[7] < 32.0:
                if input[1] < 836.0:
                    var271 = 0.07190707
                else:
                    var271 = -0.4184063
            else:
                if input[8] < 45.0:
                    var271 = 1.3860283
                else:
                    var271 = 0.17143098
        else:
            if input[2] < 2253.61:
                var271 = 2.1843786
            else:
                var271 = 0.025552368
    if input[2] < 1807.71:
        if input[2] < 1765.96:
            if input[2] < 1757.75:
                if input[8] < 33.0:
                    var272 = -0.12980828
                else:
                    var272 = 0.123168185
            else:
                var272 = -2.4442368
        else:
            if input[8] < 80.0:
                if input[0] < 2.0:
                    var272 = -0.15799867
                else:
                    var272 = 1.9987007
            else:
                var272 = -0.17751466
    else:
        if input[2] < 1880.69:
            if input[8] < 50.0:
                if input[8] < 40.0:
                    var272 = -1.3447838
                else:
                    var272 = -6.6584544
            else:
                if input[2] < 1853.57:
                    var272 = -2.109679
                else:
                    var272 = 1.1842393
        else:
            if input[4] < 149.6:
                if input[3] < 38.95:
                    var272 = 3.0366318
                else:
                    var272 = -0.33719075
            else:
                if input[3] < 893.0:
                    var272 = -0.21568346
                else:
                    var272 = 1.6622375
    if input[3] < 61.0:
        if input[3] < 59.5:
            if input[4] < 149.13777:
                if input[3] < 40.692307:
                    var273 = -0.048836976
                else:
                    var273 = -0.961049
            else:
                if input[2] < 1349.61:
                    var273 = 0.9707595
                else:
                    var273 = -0.011424167
        else:
            if input[4] < 195.534:
                var273 = -2.3844116
            else:
                var273 = 0.7333252
    else:
        if input[3] < 64.22222:
            if input[8] < 76.0:
                if input[2] < 1508.97:
                    var273 = 2.4672868
                else:
                    var273 = 0.74113363
            else:
                if input[8] < 93.0:
                    var273 = -1.4037336
                else:
                    var273 = 1.9970175
        else:
            if input[4] < 169.41692:
                if input[8] < 82.0:
                    var273 = 0.16061589
                else:
                    var273 = 1.3418294
            else:
                if input[3] < 99.545456:
                    var273 = -0.548043
                else:
                    var273 = 0.053434778
    if input[3] < 989.0:
        if input[4] < 252.57286:
            if input[4] < 245.9425:
                if input[3] < 100.6:
                    var274 = -0.105281256
                else:
                    var274 = 0.24611938
            else:
                var274 = 3.2151012
        else:
            if input[0] < 8.0:
                if input[2] < 2328.11:
                    var274 = -0.22900632
                else:
                    var274 = 0.37639585
            else:
                if input[1] < 527.0:
                    var274 = -0.18685669
                else:
                    var274 = -1.9554669
    else:
        if input[2] < 1448.55:
            if input[1] < 993.0:
                var274 = 1.1364411
            else:
                if input[1] < 1038.0:
                    var274 = -1.1661774
                else:
                    var274 = 0.3657026
        else:
            if input[1] < 993.0:
                var274 = 0.44319153
            else:
                var274 = 1.6027313
    if input[3] < 989.0:
        if input[7] < 36.0:
            if input[2] < 1143.58:
                if input[2] < 863.93:
                    var275 = 0.10289561
                else:
                    var275 = -0.59868735
            else:
                if input[2] < 1210.87:
                    var275 = 1.4760499
                else:
                    var275 = 0.024184825
        else:
            var275 = -2.3563774
    else:
        if input[2] < 1815.6:
            if input[2] < 1639.17:
                if input[1] < 1062.0:
                    var275 = 1.1094654
                else:
                    var275 = 0.24889629
            else:
                var275 = -1.2216514
        else:
            if input[1] < 993.0:
                var275 = 0.4321106
            else:
                var275 = 1.7103119
    if input[1] < 344.0:
        if input[1] < 293.0:
            if input[1] < 263.0:
                if input[2] < 78.33:
                    var276 = 0.51996285
                else:
                    var276 = -0.27589905
            else:
                if input[1] < 286.0:
                    var276 = 0.91669387
                else:
                    var276 = -0.33611044
        else:
            if input[8] < 77.0:
                if input[3] < 44.5:
                    var276 = -1.6293873
                else:
                    var276 = -0.33058363
            else:
                if input[8] < 90.0:
                    var276 = 1.0536565
                else:
                    var276 = -0.7478119
    else:
        if input[1] < 389.0:
            if input[3] < 70.25:
                if input[2] < 311.43:
                    var276 = -0.31166917
                else:
                    var276 = 2.4764225
            else:
                if input[1] < 379.0:
                    var276 = -0.60282135
                else:
                    var276 = 0.821304
        else:
            if input[3] < 40.166668:
                if input[8] < 45.0:
                    var276 = 1.844696
                else:
                    var276 = -0.029321289
            else:
                if input[1] < 463.0:
                    var276 = -0.67815757
                else:
                    var276 = -0.01097463
    if input[3] < 577.5:
        if input[3] < 356.5:
            if input[0] < 8.0:
                if input[8] < 81.0:
                    var277 = 0.23746641
                else:
                    var277 = -0.32503423
            else:
                if input[4] < 280.47:
                    var277 = -0.10304021
                else:
                    var277 = -1.8170799
        else:
            if input[8] < 58.0:
                if input[4] < 68.04667:
                    var277 = 1.2846303
                else:
                    var277 = -1.3457943
            else:
                if input[0] < 2.0:
                    var277 = -0.7280936
                else:
                    var277 = 0.6086463
    else:
        if input[1] < 1038.0:
            if input[4] < 1054.965:
                if input[4] < 128.05:
                    var277 = -0.10653382
                else:
                    var277 = 1.1248474
            else:
                if input[4] < 1300.17:
                    var277 = -1.2189417
                else:
                    var277 = 0.25300536
        else:
            if input[4] < 1697.08:
                if input[1] < 1159.0:
                    var277 = 0.43382534
                else:
                    var277 = 1.6422074
            else:
                var277 = 1.8139261
    if input[3] < 64.22222:
        if input[3] < 62.0:
            if input[3] < 57.642857:
                if input[7] < 2.0:
                    var278 = -0.014551865
                else:
                    var278 = 1.0137113
            else:
                if input[3] < 60.636364:
                    var278 = -1.3036437
                else:
                    var278 = 0.38510573
        else:
            if input[9] < 17.0:
                if input[0] < 10.0:
                    var278 = 1.2680315
                else:
                    var278 = 2.6241133
            else:
                var278 = -0.3130829
    else:
        if input[3] < 65.77778:
            if input[0] < 14.0:
                var278 = -1.4841967
            else:
                var278 = 0.03057251
        else:
            if input[8] < 89.0:
                if input[8] < 81.0:
                    var278 = -0.06005581
                else:
                    var278 = -0.7912604
            else:
                if input[2] < 1422.11:
                    var278 = 1.127961
                else:
                    var278 = -0.65286106
    if input[8] < 76.0:
        if input[2] < 1411.49:
            if input[8] < 72.0:
                if input[4] < 205.0089:
                    var279 = 0.05619181
                else:
                    var279 = -0.62208885
            else:
                if input[3] < 44.5:
                    var279 = -1.4465554
                else:
                    var279 = 1.322619
        else:
            if input[0] < 4.0:
                if input[3] < 491.5:
                    var279 = -0.65792257
                else:
                    var279 = 0.46052724
            else:
                if input[3] < 99.545456:
                    var279 = 0.08945146
                else:
                    var279 = 1.2641073
    else:
        if input[1] < 778.0:
            if input[1] < 756.0:
                if input[1] < 752.0:
                    var279 = 0.025633588
                else:
                    var279 = -1.8885742
            else:
                if input[1] < 774.0:
                    var279 = 2.9256322
                else:
                    var279 = 0.098321535
        else:
            if input[1] < 1153.0:
                if input[3] < 225.2:
                    var279 = -1.083885
                else:
                    var279 = -0.06687155
            else:
                if input[1] < 1187.0:
                    var279 = 1.0252991
                else:
                    var279 = -0.77219445
    if input[1] < 904.0:
        if input[1] < 875.0:
            if input[2] < 2077.07:
                if input[6] < 40.0:
                    var280 = 0.04890318
                else:
                    var280 = -0.96466035
            else:
                if input[8] < 12.0:
                    var280 = -0.5708624
                else:
                    var280 = 0.6460842
        else:
            if input[3] < 111.375:
                if input[0] < 11.0:
                    var280 = -1.7219397
                else:
                    var280 = 1.6941808
            else:
                if input[0] < 3.0:
                    var280 = -0.30353495
                else:
                    var280 = 2.5173023
    else:
        if input[3] < 78.75:
            if input[3] < 70.25:
                if input[1] < 959.0:
                    var280 = 0.8892395
                else:
                    var280 = -0.39071962
            else:
                if input[2] < 2400.13:
                    var280 = -3.024923
                else:
                    var280 = 0.52606815
        else:
            if input[2] < 1285.82:
                if input[3] < 145.75:
                    var280 = 1.2568551
                else:
                    var280 = -0.17239335
            else:
                if input[1] < 947.0:
                    var280 = -2.032878
                else:
                    var280 = -0.36650813
    if input[0] < 12.0:
        if input[3] < 42.333332:
            if input[1] < 447.0:
                if input[4] < 582.37:
                    var281 = -0.24926396
                else:
                    var281 = 1.1479294
            else:
                var281 = -2.4484425
        else:
            if input[0] < 11.0:
                if input[4] < 231.4943:
                    var281 = -0.23002496
                else:
                    var281 = 0.07340236
            else:
                if input[8] < 87.0:
                    var281 = 0.3080488
                else:
                    var281 = 2.1763718
    else:
        if input[2] < 2171.07:
            if input[2] < 2022.94:
                if input[2] < 517.54:
                    var281 = -0.35373133
                else:
                    var281 = 0.32984856
            else:
                if input[1] < 606.0:
                    var281 = 2.8989522
                else:
                    var281 = -1.5980958
        else:
            if input[8] < 69.0:
                if input[1] < 117.0:
                    var281 = 0.64957154
                else:
                    var281 = -1.196368
            else:
                if input[4] < 190.612:
                    var281 = 0.7613604
                else:
                    var281 = -0.3946579
    if input[8] < 8.0:
        if input[0] < 8.0:
            if input[4] < 280.47:
                if input[4] < 187.2825:
                    var282 = -0.11499369
                else:
                    var282 = 1.1673944
            else:
                if input[4] < 484.465:
                    var282 = -1.254012
                else:
                    var282 = 0.18811874
        else:
            if input[1] < 862.0:
                if input[3] < 66.666664:
                    var282 = -0.46800065
                else:
                    var282 = 1.1259034
            else:
                if input[2] < 696.14:
                    var282 = -0.30785522
                else:
                    var282 = -2.1054125
    else:
        if input[8] < 10.0:
            if input[0] < 5.0:
                if input[2] < 124.65:
                    var282 = 0.17625046
                else:
                    var282 = -1.1897949
            else:
                if input[0] < 11.0:
                    var282 = 2.619033
                else:
                    var282 = -1.0361633
        else:
            if input[1] < 616.0:
                if input[1] < 516.0:
                    var282 = 0.09529551
                else:
                    var282 = -0.6826689
            else:
                if input[1] < 633.0:
                    var282 = 1.3900732
                else:
                    var282 = 0.19396286
    if input[4] < 39.6625:
        if input[4] < 21.13:
            if input[4] < 16.933332:
                if input[0] < 14.0:
                    var283 = -0.32181808
                else:
                    var283 = 1.8959411
            else:
                if input[0] < 14.0:
                    var283 = 1.2687849
                else:
                    var283 = -1.7969483
        else:
            if input[8] < 97.0:
                if input[1] < 195.73:
                    var283 = 0.36243373
                else:
                    var283 = -0.99446136
            else:
                if input[0] < 5.0:
                    var283 = -0.10336914
                else:
                    var283 = 2.426584
    else:
        if input[4] < 47.13:
            if input[2] < 477.17:
                if input[4] < 43.54625:
                    var283 = -0.3827716
                else:
                    var283 = 1.2849452
            else:
                var283 = 3.003495
        else:
            if input[2] < 221.15:
                if input[0] < 2.0:
                    var283 = -0.1442763
                else:
                    var283 = 2.0401034
            else:
                if input[2] < 285.5:
                    var283 = -1.310273
                else:
                    var283 = 0.07614775
    if input[0] < 9.0:
        if input[0] < 8.0:
            if input[8] < 82.0:
                if input[1] < 751.0:
                    var284 = 0.0062044477
                else:
                    var284 = 0.34029797
            else:
                if input[9] < 8.0:
                    var284 = -1.149722
                else:
                    var284 = 0.17928155
        else:
            if input[8] < 30.0:
                if input[1] < 301.0:
                    var284 = -0.40406036
                else:
                    var284 = -2.4564211
            else:
                if input[1] < 798.0:
                    var284 = -0.6889333
                else:
                    var284 = 1.048466
    else:
        if input[7] < 4.0:
            if input[3] < 88.6:
                if input[8] < 30.0:
                    var284 = 0.72476196
                else:
                    var284 = 0.12325811
            else:
                if input[2] < 497.7:
                    var284 = 0.61965483
                else:
                    var284 = -0.98756105
        else:
            if input[3] < 107.57143:
                if input[8] < 4.0:
                    var284 = -0.88551027
                else:
                    var284 = 2.27337
            else:
                if input[1] < 1086.0:
                    var284 = -1.1547703
                else:
                    var284 = 1.0558221
    if input[4] < 66.496155:
        if input[2] < 555.49:
            if input[1] < 793.0:
                if input[1] < 725.0:
                    var285 = 0.21245597
                else:
                    var285 = -1.4428757
            else:
                if input[8] < 70.0:
                    var285 = 0.34957972
                else:
                    var285 = 1.7767429
        else:
            if input[2] < 808.38:
                if input[1] < 965.0:
                    var285 = 2.1534986
                else:
                    var285 = -0.60695803
            else:
                if input[1] < 175.0:
                    var285 = -0.9671163
                else:
                    var285 = 0.52837527
    else:
        if input[4] < 66.75667:
            if input[1] < 104.0:
                var285 = 0.31678924
            else:
                var285 = -3.1409378
        else:
            if input[1] < 198.0:
                if input[1] < 175.0:
                    var285 = -0.18382953
                else:
                    var285 = -1.4494001
            else:
                if input[3] < 131.8:
                    var285 = 0.1850644
                else:
                    var285 = -0.14095414
    if input[3] < 252.75:
        if input[3] < 210.0:
            if input[2] < 1070.22:
                if input[4] < 182.08:
                    var286 = -0.33217517
                else:
                    var286 = 0.564392
            else:
                if input[8] < 49.0:
                    var286 = 0.23013055
                else:
                    var286 = -0.26437113
        else:
            if input[4] < 511.77:
                if input[1] < 1122.0:
                    var286 = -1.8500384
                else:
                    var286 = -0.037210084
            else:
                if input[1] < 844.0:
                    var286 = -0.15502778
                else:
                    var286 = 2.1158164
    else:
        if input[3] < 261.75:
            if input[4] < 616.0725:
                var286 = 2.7855537
            else:
                if input[1] < 770.0:
                    var286 = 1.0435506
                else:
                    var286 = -0.5506622
        else:
            if input[4] < 68.04667:
                if input[8] < 38.0:
                    var286 = 1.5659932
                else:
                    var286 = -0.4908104
            else:
                if input[3] < 388.0:
                    var286 = -0.3652542
                else:
                    var286 = 0.20720902
    if input[1] < 965.0:
        if input[5] < 19.0:
            if input[1] < 333.0:
                if input[1] < 296.0:
                    var287 = -0.04611364
                else:
                    var287 = -0.84626
            else:
                if input[1] < 424.0:
                    var287 = 0.6674296
                else:
                    var287 = 0.026219934
        else:
            if input[8] < 63.0:
                if input[3] < 136.14285:
                    var287 = 2.8680685
                else:
                    var287 = -0.79160464
            else:
                if input[0] < 12.0:
                    var287 = -0.7236066
                else:
                    var287 = 0.93573
    else:
        if input[1] < 989.0:
            if input[8] < 93.0:
                if input[0] < 13.0:
                    var287 = -2.437557
                else:
                    var287 = -0.39704895
            else:
                var287 = 0.30662537
        else:
            if input[0] < 3.0:
                if input[4] < 1054.965:
                    var287 = 1.3443912
                else:
                    var287 = 0.17600988
            else:
                if input[4] < 133.09222:
                    var287 = 0.28886378
                else:
                    var287 = -0.6760462
    if input[1] < 1162.0:
        if input[1] < 1145.0:
            if input[4] < 287.00876:
                if input[4] < 231.4943:
                    var288 = -0.020665484
                else:
                    var288 = 0.80877334
            else:
                if input[8] < 68.0:
                    var288 = -0.3309246
                else:
                    var288 = 0.2309541
        else:
            if input[8] < 44.0:
                if input[0] < 9.0:
                    var288 = -0.5247223
                else:
                    var288 = 2.079948
            else:
                if input[8] < 82.0:
                    var288 = -2.383314
                else:
                    var288 = -0.19002533
    else:
        if input[0] < 5.0:
            if input[7] < 16.0:
                if input[2] < 2166.02:
                    var288 = -1.6408573
                else:
                    var288 = 1.3939942
            else:
                if input[0] < 3.0:
                    var288 = 1.513318
                else:
                    var288 = 0.121844485
        else:
            if input[4] < 2.850909:
                if input[0] < 11.0:
                    var288 = -1.4170716
                else:
                    var288 = 0.079272464
            else:
                if input[1] < 1187.0:
                    var288 = 1.8931717
                else:
                    var288 = 0.6148987
    if input[4] < 71.902:
        if input[4] < 70.6:
            if input[2] < 808.38:
                if input[2] < 735.52:
                    var289 = 0.07254761
                else:
                    var289 = 2.925112
            else:
                if input[8] < 29.0:
                    var289 = 1.2591873
                else:
                    var289 = -2.39996
        else:
            if input[1] < 131.0:
                var289 = 1.1864299
            else:
                var289 = 3.6755097
    else:
        if input[4] < 93.88143:
            if input[7] < 5.0:
                if input[1] < 934.0:
                    var289 = -0.80696887
                else:
                    var289 = 2.3951705
            else:
                if input[1] < 752.0:
                    var289 = 0.9717911
                else:
                    var289 = -2.9470232
        else:
            if input[4] < 95.216:
                if input[1] < 951.0:
                    var289 = 3.6397247
                else:
                    var289 = -2.5447145
            else:
                if input[0] < 8.0:
                    var289 = 0.062156703
                else:
                    var289 = -0.3287833
    if input[1] < 586.0:
        if input[1] < 560.0:
            if input[4] < 375.698:
                if input[0] < 8.0:
                    var290 = 0.3822063
                else:
                    var290 = -0.13245235
            else:
                if input[4] < 378.305:
                    var290 = -3.5390084
                else:
                    var290 = -0.39111525
        else:
            if input[4] < 316.74667:
                if input[8] < 80.0:
                    var290 = -2.444322
                else:
                    var290 = 0.27502748
            else:
                if input[0] < 3.0:
                    var290 = 0.03425293
                else:
                    var290 = 0.7256317
    else:
        if input[1] < 606.0:
            if input[1] < 601.0:
                if input[4] < 88.365:
                    var290 = -0.29470277
                else:
                    var290 = 1.4174306
            else:
                var290 = 3.515387
        else:
            if input[1] < 774.0:
                if input[1] < 756.0:
                    var290 = 0.19360588
                else:
                    var290 = 1.5018651
            else:
                if input[8] < 84.0:
                    var290 = 0.17349891
                else:
                    var290 = -0.6416742
    if input[1] < 958.0:
        if input[1] < 904.0:
            if input[2] < 863.93:
                if input[8] < 84.0:
                    var291 = 0.31731543
                else:
                    var291 = -0.45565733
            else:
                if input[2] < 1249.41:
                    var291 = -0.48904735
                else:
                    var291 = 0.10253109
        else:
            if input[8] < 88.0:
                if input[3] < 85.0:
                    var291 = -2.3352983
                else:
                    var291 = -0.46262702
            else:
                if input[8] < 92.0:
                    var291 = 3.9555604
                else:
                    var291 = 0.4668799
    else:
        if input[3] < 145.75:
            if input[3] < 142.5:
                if input[2] < 540.6:
                    var291 = -0.74346584
                else:
                    var291 = 0.6922481
            else:
                if input[2] < 1516.42:
                    var291 = 5.2570496
                else:
                    var291 = 0.46329752
        else:
            if input[3] < 154.0:
                if input[2] < 555.49:
                    var291 = 1.0772014
                else:
                    var291 = -2.3772914
            else:
                if input[9] < 77.0:
                    var291 = -0.10476696
                else:
                    var291 = 1.4267017
    if input[2] < 2035.17:
        if input[4] < 375.698:
            if input[4] < 231.4943:
                if input[4] < 219.127:
                    var292 = 0.035096604
                else:
                    var292 = -1.4049249
            else:
                if input[8] < 50.0:
                    var292 = -0.08628055
                else:
                    var292 = 1.22831
        else:
            if input[0] < 5.0:
                if input[2] < 834.06:
                    var292 = 0.820477
                else:
                    var292 = -0.47482482
            else:
                if input[2] < 1880.69:
                    var292 = -8.400583
                else:
                    var292 = 0.3116562
    else:
        if input[0] < 6.0:
            if input[4] < 476.764:
                if input[1] < 782.17:
                    var292 = 2.0485687
                else:
                    var292 = -0.04634247
            else:
                if input[4] < 544.2833:
                    var292 = -0.8373246
                else:
                    var292 = 0.19059175
        else:
            if input[2] < 2218.74:
                if input[8] < 62.0:
                    var292 = -1.4183638
                else:
                    var292 = -0.44357607
            else:
                if input[2] < 2235.72:
                    var292 = 1.10719
                else:
                    var292 = -0.50493145
    if input[1] < 1145.0:
        if input[6] < 14.0:
            if input[2] < 655.24:
                if input[8] < 10.0:
                    var293 = 0.64509207
                else:
                    var293 = -0.124524556
            else:
                if input[4] < 70.6:
                    var293 = 0.8032857
                else:
                    var293 = -2.8034909
        else:
            if input[4] < 86.75:
                if input[3] < 72.666664:
                    var293 = -0.2349584
                else:
                    var293 = 4.099678
            else:
                if input[2] < 735.52:
                    var293 = 1.3416326
                else:
                    var293 = 0.025952077
    else:
        if input[3] < 399.0:
            if input[2] < 1639.17:
                if input[2] < 555.49:
                    var293 = 0.19266832
                else:
                    var293 = -2.0848422
            else:
                if input[1] < 1185.0:
                    var293 = -0.47479358
                else:
                    var293 = 0.9449158
        else:
            var293 = 1.5820191
    if input[1] < 597.0:
        if input[1] < 560.0:
            if input[4] < 375.698:
                if input[3] < 78.5:
                    var294 = -0.09546029
                else:
                    var294 = 0.6558256
            else:
                if input[4] < 378.305:
                    var294 = -3.3040664
                else:
                    var294 = -0.3597026
        else:
            if input[0] < 14.0:
                if input[4] < 173.92125:
                    var294 = -2.4165182
                else:
                    var294 = -0.33002663
            else:
                if input[8] < 62.0:
                    var294 = 1.285439
                else:
                    var294 = -0.9396576
    else:
        if input[3] < 51.25:
            if input[3] < 44.11111:
                var294 = -0.55915326
            else:
                if input[3] < 47.909092:
                    var294 = 1.098885
                else:
                    var294 = 3.3124511
        else:
            if input[1] < 606.0:
                var294 = 2.0931191
            else:
                if input[7] < 4.0:
                    var294 = -0.28848848
                else:
                    var294 = 0.07609456
    var295 = var239 + var240 + var241 + var242 + var243 + var244 + var245 + var246 + var247 + var248 + var249 + var250 + var251 + var252 + var253 + var254 + var255 + var256 + var257 + var258 + var259 + var260 + var261 + var262 + var263 + var264 + var265 + var266 + var267 + var268 + var269 + var270 + var271 + var272 + var273 + var274 + var275 + var276 + var277 + var278 + var279 + var280 + var281 + var282 + var283 + var284 + var285 + var286 + var287 + var288 + var289 + var290 + var291 + var292 + var293 + var294
    if input[4] < 71.902:
        if input[4] < 70.6:
            if input[1] < 1080.0:
                if input[1] < 1029.0:
                    var296 = 0.16652878
                else:
                    var296 = 1.713638
            else:
                if input[8] < 44.0:
                    var296 = 1.2927498
                else:
                    var296 = -1.4275893
        else:
            if input[1] < 622.0:
                var296 = 1.4164475
            else:
                var296 = 3.4658172
    else:
        if input[4] < 75.08583:
            if input[1] < 751.0:
                if input[1] < 229.0:
                    var296 = -0.74640405
                else:
                    var296 = 0.3303589
            else:
                var296 = -2.6380057
        else:
            if input[4] < 76.43846:
                var296 = 1.6335458
            else:
                if input[4] < 84.632:
                    var296 = -0.8395856
                else:
                    var296 = -0.03984123
    if input[1] < 1166.0:
        if input[1] < 1070.0:
            if input[1] < 1020.0:
                if input[1] < 1012.0:
                    var297 = 0.0064997016
                else:
                    var297 = -1.9636475
            else:
                if input[3] < 128.33333:
                    var297 = 1.6439396
                else:
                    var297 = 0.10695384
        else:
            if input[1] < 1086.0:
                if input[0] < 11.0:
                    var297 = -1.821997
                else:
                    var297 = 0.49878174
            else:
                if input[9] < 6.0:
                    var297 = 0.6091756
                else:
                    var297 = -0.5153752
    else:
        if input[8] < 92.0:
            if input[8] < 88.0:
                if input[9] < 22.0:
                    var297 = 0.377892
                else:
                    var297 = 1.4853195
            else:
                var297 = -1.0938781
        else:
            var297 = 1.8784342
    if input[2] < 1358.14:
        if input[2] < 1346.21:
            if input[3] < 136.14285:
                if input[1] < 836.0:
                    var298 = 0.039588355
                else:
                    var298 = 0.6968741
            else:
                if input[3] < 141.0:
                    var298 = -2.399414
                else:
                    var298 = -0.052088596
        else:
            if input[0] < 11.0:
                var298 = 3.3504655
            else:
                if input[0] < 12.0:
                    var298 = -0.575
                else:
                    var298 = 0.35797426
    else:
        if input[4] < 176.572:
            if input[8] < 76.0:
                if input[8] < 48.0:
                    var298 = -0.5124607
                else:
                    var298 = -2.1913524
            else:
                if input[3] < 88.6:
                    var298 = 0.9246451
                else:
                    var298 = -0.8625814
        else:
            if input[4] < 219.127:
                if input[8] < 87.0:
                    var298 = 0.7005009
                else:
                    var298 = -0.8099858
            else:
                if input[1] < 1062.0:
                    var298 = -0.0095153535
                else:
                    var298 = -0.8740722
    if input[2] < 477.17:
        if input[3] < 49.333332:
            if input[3] < 18.166666:
                if input[0] < 14.0:
                    var299 = -0.3568922
                else:
                    var299 = 2.359085
            else:
                if input[2] < 137.84:
                    var299 = 0.15107638
                else:
                    var299 = 1.380285
        else:
            if input[3] < 61.0:
                if input[2] < 239.64:
                    var299 = -0.18411331
                else:
                    var299 = -1.9688667
            else:
                if input[3] < 72.85714:
                    var299 = 1.4125074
                else:
                    var299 = 0.03958024
    else:
        if input[4] < 37.923077:
            var299 = -3.3685749
        else:
            if input[4] < 101.346664:
                if input[4] < 71.902:
                    var299 = 0.1628604
                else:
                    var299 = -0.6625123
            else:
                if input[3] < 56.636364:
                    var299 = 0.26838598
                else:
                    var299 = -0.13123485
    if input[4] < 40.83286:
        if input[2] < 350.58:
            if input[3] < 73.55556:
                if input[1] < 85.0:
                    var300 = -0.69207245
                else:
                    var300 = 0.67938656
            else:
                if input[6] < 3.0:
                    var300 = 0.048326537
                else:
                    var300 = -1.1971501
        else:
            if input[8] < 3.0:
                var300 = 1.1506866
            else:
                if input[8] < 69.0:
                    var300 = -2.2797348
                else:
                    var300 = -0.4622821
    else:
        if input[4] < 71.902:
            if input[4] < 70.6:
                if input[4] < 69.535:
                    var300 = 0.5781276
                else:
                    var300 = -1.6708908
            else:
                if input[1] < 131.0:
                    var300 = 1.1098247
                else:
                    var300 = 3.3575165
        else:
            if input[0] < 8.0:
                if input[0] < 4.0:
                    var300 = -0.06873433
                else:
                    var300 = 0.43388033
            else:
                if input[8] < 74.0:
                    var300 = -0.34963673
                else:
                    var300 = 0.47550806
    if input[8] < 47.0:
        if input[0] < 8.0:
            if input[8] < 45.0:
                if input[3] < 130.2:
                    var301 = 0.4885288
                else:
                    var301 = -0.010952404
            else:
                if input[1] < 1001.0:
                    var301 = 1.6755837
                else:
                    var301 = 0.119590245
        else:
            if input[3] < 145.75:
                if input[8] < 45.0:
                    var301 = -0.020313889
                else:
                    var301 = -1.7585633
            else:
                var301 = -3.3286054
    else:
        if input[8] < 50.0:
            if input[2] < 484.34:
                if input[8] < 49.0:
                    var301 = -0.8531643
                else:
                    var301 = 1.9157412
            else:
                if input[8] < 49.0:
                    var301 = 0.4348131
                else:
                    var301 = -4.568273
        else:
            if input[2] < 364.79:
                if input[4] < 24.540909:
                    var301 = 0.30829862
                else:
                    var301 = -0.9439228
            else:
                if input[0] < 2.0:
                    var301 = -0.5335694
                else:
                    var301 = 0.09005113
    if input[1] < 1086.0:
        if input[1] < 1070.0:
            if input[4] < 1143.58:
                if input[4] < 809.63:
                    var302 = 0.008223203
                else:
                    var302 = 0.72318953
            else:
                if input[3] < 697.0:
                    var302 = -0.8072052
                else:
                    var302 = 0.07342027
        else:
            if input[2] < 171.32:
                var302 = 1.3227112
            else:
                if input[3] < 89.666664:
                    var302 = 0.36797944
                else:
                    var302 = -1.9821233
    else:
        if input[3] < 82.166664:
            var302 = 1.8537171
        else:
            if input[3] < 88.8:
                if input[1] < 1159.0:
                    var302 = -2.135721
                else:
                    var302 = -0.24423218
            else:
                if input[8] < 27.0:
                    var302 = -0.4304587
                else:
                    var302 = 0.6693337
    if input[2] < 863.93:
        if input[6] < 14.0:
            if input[2] < 672.91:
                if input[8] < 10.0:
                    var303 = 0.5542739
                else:
                    var303 = -0.11438798
            else:
                if input[3] < 91.666664:
                    var303 = -0.55297244
                else:
                    var303 = -2.9760041
        else:
            if input[3] < 601.0:
                if input[8] < 99.0:
                    var303 = 1.0916623
                else:
                    var303 = -1.6259292
            else:
                var303 = -1.8737081
    else:
        if input[2] < 910.41:
            if input[1] < 275.0:
                if input[1] < 222.0:
                    var303 = -1.909433
                else:
                    var303 = 0.9130959
            else:
                if input[8] < 38.0:
                    var303 = -1.172435
                else:
                    var303 = -2.895867
        else:
            if input[2] < 927.74:
                if input[3] < 77.23077:
                    var303 = 2.9436767
                else:
                    var303 = 0.60582036
            else:
                if input[2] < 1114.96:
                    var303 = -0.44334456
                else:
                    var303 = 0.0032161195
    if input[8] < 49.0:
        if input[8] < 31.0:
            if input[0] < 13.0:
                if input[3] < 79.916664:
                    var304 = 0.16558486
                else:
                    var304 = -0.37082553
            else:
                if input[1] < 532.0:
                    var304 = 2.3094423
                else:
                    var304 = 0.49858007
        else:
            if input[0] < 10.0:
                if input[6] < 23.0:
                    var304 = 0.2133621
                else:
                    var304 = 1.3096457
            else:
                if input[1] < 770.0:
                    var304 = 0.084027305
                else:
                    var304 = -1.5373837
    else:
        if input[8] < 50.0:
            if input[6] < 12.0:
                if input[6] < 8.0:
                    var304 = 1.9703311
                else:
                    var304 = -0.982694
            else:
                if input[0] < 5.0:
                    var304 = -2.8838754
                else:
                    var304 = -7.372603
        else:
            if input[4] < 21.13:
                if input[1] < 1080.0:
                    var304 = 0.92797196
                else:
                    var304 = -1.4608765
            else:
                if input[4] < 43.54625:
                    var304 = -0.8626906
                else:
                    var304 = -0.03538185
    if input[0] < 14.0:
        if input[0] < 10.0:
            if input[0] < 8.0:
                if input[8] < 10.0:
                    var305 = 0.54725593
                else:
                    var305 = -0.020670721
            else:
                if input[2] < 350.58:
                    var305 = 0.8577471
                else:
                    var305 = -0.5243048
        else:
            if input[3] < 61.666668:
                if input[0] < 12.0:
                    var305 = -0.41137657
                else:
                    var305 = 0.31984636
            else:
                if input[1] < 816.0:
                    var305 = 1.8963412
                else:
                    var305 = 0.15137759
    else:
        if input[1] < 770.0:
            if input[8] < 65.0:
                if input[8] < 27.0:
                    var305 = -0.34005737
                else:
                    var305 = 1.5429627
            else:
                if input[2] < 449.83:
                    var305 = 0.21513902
                else:
                    var305 = -2.0414796
        else:
            if input[8] < 26.0:
                if input[1] < 868.0:
                    var305 = -0.85365754
                else:
                    var305 = 1.7771606
            else:
                if input[2] < 1249.41:
                    var305 = -2.3062093
                else:
                    var305 = -0.6967155
    if input[8] < 49.0:
        if input[8] < 27.0:
            if input[3] < 89.22222:
                if input[6] < 17.0:
                    var306 = 0.8186678
                else:
                    var306 = 0.046427082
            else:
                if input[3] < 154.0:
                    var306 = -0.8076858
                else:
                    var306 = 0.0482175
        else:
            if input[4] < 39.6625:
                if input[8] < 34.0:
                    var306 = -1.4995497
                else:
                    var306 = -0.23523799
            else:
                if input[4] < 45.59:
                    var306 = 3.1017206
                else:
                    var306 = 0.4713702
    else:
        if input[8] < 50.0:
            if input[6] < 10.0:
                if input[0] < 4.0:
                    var306 = 0.32904485
                else:
                    var306 = 2.485252
            else:
                if input[1] < 522.0:
                    var306 = -6.591802
                else:
                    var306 = -1.6298914
        else:
            if input[8] < 57.0:
                if input[0] < 10.0:
                    var306 = 0.14943357
                else:
                    var306 = 1.7801415
            else:
                if input[3] < 250.0:
                    var306 = -0.19915041
                else:
                    var306 = 0.3567996
    if input[4] < 219.127:
        if input[4] < 206.61363:
            if input[1] < 1020.0:
                if input[1] < 1012.0:
                    var307 = 0.0033446539
                else:
                    var307 = -2.2934473
            else:
                if input[3] < 143.0:
                    var307 = 0.85665226
                else:
                    var307 = -0.34005663
        else:
            if input[2] < 1922.45:
                if input[8] < 80.0:
                    var307 = 2.2717557
                else:
                    var307 = 0.0916626
            else:
                if input[0] < 11.0:
                    var307 = -0.3807597
                else:
                    var307 = 1.0059518
    else:
        if input[0] < 8.0:
            if input[8] < 55.0:
                if input[8] < 49.0:
                    var307 = 0.0076441676
                else:
                    var307 = -1.3248605
            else:
                if input[4] < 252.57286:
                    var307 = 2.0665643
                else:
                    var307 = 0.09390179
        else:
            if input[1] < 527.0:
                if input[0] < 9.0:
                    var307 = -0.67490506
                else:
                    var307 = 1.128003
            else:
                if input[1] < 868.0:
                    var307 = -2.1635873
                else:
                    var307 = -0.74862176
    if input[0] < 7.0:
        if input[3] < 95.4:
            if input[1] < 414.0:
                if input[8] < 18.0:
                    var308 = 0.8153844
                else:
                    var308 = -0.029740414
            else:
                if input[1] < 470.0:
                    var308 = 2.240621
                else:
                    var308 = 0.4911972
        else:
            if input[3] < 109.888885:
                if input[4] < 302.982:
                    var308 = -0.1614293
                else:
                    var308 = -3.88401
            else:
                if input[6] < 34.0:
                    var308 = -0.34051093
                else:
                    var308 = 0.3053808
    else:
        if input[7] < 4.0:
            if input[3] < 89.22222:
                if input[1] < 1145.0:
                    var308 = 0.103665866
                else:
                    var308 = -1.6825342
            else:
                if input[1] < 1014.0:
                    var308 = -1.5027964
                else:
                    var308 = 0.27988967
        else:
            if input[6] < 34.0:
                if input[6] < 14.0:
                    var308 = -0.045574952
                else:
                    var308 = 2.1997478
            else:
                if input[3] < 105.42857:
                    var308 = 1.7697865
                else:
                    var308 = -0.56827444
    if input[3] < 491.5:
        if input[4] < 1191.195:
            if input[4] < 562.6275:
                if input[4] < 375.698:
                    var309 = 0.037155095
                else:
                    var309 = -0.6072427
            else:
                if input[4] < 616.0725:
                    var309 = 1.699132
                else:
                    var309 = 0.06255021
        else:
            if input[1] < 45.0:
                if input[1] < 41.0:
                    var309 = 0.27983093
                else:
                    var309 = -0.201297
            else:
                if input[8] < 71.0:
                    var309 = -1.2472425
                else:
                    var309 = -0.4735901
    else:
        if input[8] < 76.0:
            if input[2] < 1549.86:
                if input[3] < 673.0:
                    var309 = 1.0282356
                else:
                    var309 = -0.11302032
            else:
                if input[2] < 2152.66:
                    var309 = 1.6551365
                else:
                    var309 = 0.3042694
        else:
            if input[8] < 85.0:
                if input[2] < 1291.33:
                    var309 = -1.396402
                else:
                    var309 = 0.47352502
            else:
                if input[1] < 741.0:
                    var309 = -0.31960756
                else:
                    var309 = 0.65763324
    if input[4] < 135.67334:
        if input[4] < 134.582:
            if input[2] < 39.86:
                if input[1] < 66.13:
                    var310 = -0.4944663
                else:
                    var310 = 0.66423136
            else:
                if input[2] < 47.46:
                    var310 = -2.509491
                else:
                    var310 = -0.17832844
        else:
            var310 = -2.921218
    else:
        if input[2] < 1203.1:
            if input[1] < 622.0:
                if input[3] < 40.166668:
                    var310 = -0.04580953
                else:
                    var310 = 1.0350512
            else:
                if input[3] < 143.71428:
                    var310 = -1.535746
                else:
                    var310 = 0.1525066
        else:
            if input[2] < 1422.11:
                if input[1] < 1145.0:
                    var310 = -0.6336782
                else:
                    var310 = 1.2904582
            else:
                if input[2] < 1508.97:
                    var310 = 0.96559733
                else:
                    var310 = -0.020333357
    if input[3] < 63.1:
        if input[3] < 62.0:
            if input[9] < 4.0:
                if input[8] < 50.0:
                    var311 = 0.2546558
                else:
                    var311 = -0.43304965
            else:
                if input[1] < 713.0:
                    var311 = 0.28403097
                else:
                    var311 = -1.2807983
        else:
            if input[2] < 591.44:
                if input[0] < 7.0:
                    var311 = -1.2471542
                else:
                    var311 = 1.4503449
            else:
                var311 = 2.2816355
    else:
        if input[1] < 697.0:
            if input[1] < 659.0:
                if input[2] < 863.93:
                    var311 = 0.15195173
                else:
                    var311 = -0.4189933
            else:
                if input[9] < 11.0:
                    var311 = -1.8805472
                else:
                    var311 = -0.19435807
        else:
            if input[1] < 718.0:
                if input[8] < 24.0:
                    var311 = 0.0065307617
                else:
                    var311 = 1.1661105
            else:
                if input[8] < 32.0:
                    var311 = -0.2856291
                else:
                    var311 = 0.069166675
    if input[1] < 1096.0:
        if input[1] < 1038.0:
            if input[1] < 1020.0:
                if input[1] < 1012.0:
                    var312 = -0.0023316266
                else:
                    var312 = -1.7367314
            else:
                if input[0] < 11.0:
                    var312 = 2.3885782
                else:
                    var312 = 0.06443889
        else:
            if input[0] < 2.0:
                if input[1] < 1070.0:
                    var312 = 0.96652406
                else:
                    var312 = 0.26461336
            else:
                if input[0] < 11.0:
                    var312 = -1.0160741
                else:
                    var312 = 0.27843627
    else:
        if input[1] < 1116.0:
            if input[8] < 31.0:
                if input[0] < 2.0:
                    var312 = 0.09108277
                else:
                    var312 = 0.88022965
            else:
                if input[4] < 61.13727:
                    var312 = 0.3123291
                else:
                    var312 = 2.2952545
        else:
            if input[8] < 81.0:
                if input[8] < 73.0:
                    var312 = 0.101975694
                else:
                    var312 = 2.2162902
            else:
                if input[4] < 203.704:
                    var312 = 0.14497545
                else:
                    var312 = -1.3397322
    if input[1] < 1109.0:
        if input[1] < 1012.0:
            if input[1] < 1006.0:
                if input[8] < 10.0:
                    var313 = 0.32336992
                else:
                    var313 = 0.015290077
            else:
                if input[8] < 53.0:
                    var313 = 2.4745834
                else:
                    var313 = -2.0362387
        else:
            if input[1] < 1020.0:
                var313 = -1.9633108
            else:
                if input[0] < 11.0:
                    var313 = -0.51176053
                else:
                    var313 = 0.6426636
    else:
        if input[8] < 70.0:
            if input[8] < 30.0:
                if input[2] < 818.99:
                    var313 = 1.5329361
                else:
                    var313 = 0.29716516
            else:
                if input[3] < 140.0:
                    var313 = -1.2205151
                else:
                    var313 = 0.25559694
        else:
            if input[4] < 125.935:
                var313 = 2.7182567
            else:
                if input[8] < 87.0:
                    var313 = 1.1726006
                else:
                    var313 = -0.6293072
    if input[8] < 49.0:
        if input[3] < 18.166666:
            if input[8] < 6.0:
                if input[1] < 59.0:
                    var314 = -0.45078608
                else:
                    var314 = 1.2801294
            else:
                if input[3] < 2.5:
                    var314 = -0.07409363
                else:
                    var314 = -0.9676262
        else:
            if input[3] < 20.545454:
                var314 = 2.115036
            else:
                if input[1] < 1153.0:
                    var314 = 0.05278747
                else:
                    var314 = 0.84267473
    else:
        if input[8] < 50.0:
            if input[2] < 716.7:
                if input[2] < 407.43:
                    var314 = 1.5408095
                else:
                    var314 = -1.3320211
            else:
                if input[0] < 5.0:
                    var314 = -2.4733164
                else:
                    var314 = -6.7407546
        else:
            if input[4] < 200.6425:
                if input[3] < 9.375:
                    var314 = 0.58086234
                else:
                    var314 = -0.30650142
            else:
                if input[4] < 302.982:
                    var314 = 0.6122197
                else:
                    var314 = -0.121330395
    if input[1] < 904.0:
        if input[1] < 872.0:
            if input[4] < 133.09222:
                if input[6] < 18.0:
                    var315 = 0.01658747
                else:
                    var315 = -0.7703246
            else:
                if input[1] < 836.0:
                    var315 = 0.17304814
                else:
                    var315 = -0.74172443
        else:
            if input[3] < 111.375:
                if input[3] < 88.6:
                    var315 = 1.2559911
                else:
                    var315 = -1.701116
            else:
                if input[0] < 3.0:
                    var315 = -0.45774308
                else:
                    var315 = 1.801857
    else:
        if input[1] < 941.0:
            if input[8] < 86.0:
                if input[8] < 4.0:
                    var315 = -0.36868083
                else:
                    var315 = -2.215637
            else:
                if input[2] < 1049.84:
                    var315 = 3.168676
                else:
                    var315 = -0.2401347
        else:
            if input[8] < 75.0:
                if input[8] < 73.0:
                    var315 = 0.020512294
                else:
                    var315 = 2.3044639
            else:
                if input[2] < 834.06:
                    var315 = 0.2653978
                else:
                    var315 = -0.88209194
    if input[1] < 532.0:
        if input[1] < 483.0:
            if input[8] < 93.0:
                if input[4] < 492.1575:
                    var316 = 0.21168797
                else:
                    var316 = -0.29147437
            else:
                if input[1] < 123.0:
                    var316 = 0.44892222
                else:
                    var316 = -0.8472044
        else:
            if input[8] < 30.0:
                var316 = 2.8095424
            else:
                if input[3] < 59.0:
                    var316 = 0.038905922
                else:
                    var316 = 1.6298752
    else:
        if input[4] < 349.68857:
            if input[4] < 219.127:
                if input[1] < 993.0:
                    var316 = -0.15146576
                else:
                    var316 = 0.4260086
            else:
                if input[8] < 45.0:
                    var316 = -1.4818177
                else:
                    var316 = -0.32621723
        else:
            if input[3] < 181.0:
                if input[2] < 2385.6:
                    var316 = 2.0416124
                else:
                    var316 = -0.68190306
            else:
                if input[9] < 20.0:
                    var316 = -0.4124774
                else:
                    var316 = 0.34615824
    if input[0] < 9.0:
        if input[4] < 190.612:
            if input[2] < 1241.21:
                if input[2] < 1143.58:
                    var317 = -0.26877177
                else:
                    var317 = 2.1759183
            else:
                if input[1] < 753.0:
                    var317 = -2.3341892
                else:
                    var317 = 0.15664215
        else:
            if input[4] < 195.534:
                if input[2] < 954.02:
                    var317 = -0.6141093
                else:
                    var317 = 2.4212854
            else:
                if input[8] < 50.0:
                    var317 = -0.24569754
                else:
                    var317 = 0.19284268
    else:
        if input[1] < 482.0:
            if input[2] < 1171.99:
                if input[1] < 447.0:
                    var317 = -0.27314898
                else:
                    var317 = -1.6175364
            else:
                if input[0] < 10.0:
                    var317 = 1.4688731
                else:
                    var317 = 0.19766611
        else:
            if input[3] < 41.076923:
                if input[2] < 530.44:
                    var317 = 0.16288047
                else:
                    var317 = 2.6800935
            else:
                if input[2] < 2235.72:
                    var317 = 0.30865648
                else:
                    var317 = -0.67121387
    if input[3] < 141.0:
        if input[3] < 136.14285:
            if input[3] < 135.42857:
                if input[3] < 69.71429:
                    var318 = 0.05548296
                else:
                    var318 = -0.2488005
            else:
                var318 = 2.4518778
        else:
            if input[0] < 3.0:
                if input[8] < 72.0:
                    var318 = 0.52837294
                else:
                    var318 = -0.13006477
            else:
                if input[8] < 77.0:
                    var318 = -1.2678121
                else:
                    var318 = -3.474416
    else:
        if input[3] < 145.75:
            if input[1] < 1001.0:
                if input[8] < 24.0:
                    var318 = -0.959383
                else:
                    var318 = 1.2909774
            else:
                if input[1] < 1145.0:
                    var318 = 4.700374
                else:
                    var318 = -0.15342712
        else:
            if input[3] < 147.33333:
                if input[8] < 26.0:
                    var318 = -3.3094451
                else:
                    var318 = 0.29997253
            else:
                if input[1] < 1046.0:
                    var318 = 0.23042925
                else:
                    var318 = -0.18841963
    if input[8] < 87.0:
        if input[8] < 85.0:
            if input[1] < 1185.0:
                if input[4] < 4.44:
                    var319 = 0.8120513
                else:
                    var319 = -0.051312752
            else:
                if input[4] < 375.698:
                    var319 = 0.48821074
                else:
                    var319 = 1.4462422
        else:
            if input[1] < 1053.0:
                if input[1] < 353.0:
                    var319 = -0.047828723
                else:
                    var319 = -2.4261994
            else:
                var319 = 1.3751485
    else:
        if input[8] < 92.0:
            if input[3] < 131.8:
                if input[3] < 47.909092:
                    var319 = 0.36223713
                else:
                    var319 = 2.3772085
            else:
                if input[3] < 156.75:
                    var319 = -3.0589204
                else:
                    var319 = 0.032710128
        else:
            if input[3] < 135.42857:
                if input[4] < 8.236:
                    var319 = 1.6442267
                else:
                    var319 = -0.40533438
            else:
                if input[8] < 95.0:
                    var319 = 1.2140598
                else:
                    var319 = 0.07742282
    if input[1] < 697.0:
        if input[1] < 636.0:
            if input[1] < 597.0:
                if input[1] < 516.0:
                    var320 = -0.027994126
                else:
                    var320 = -0.6917774
            else:
                if input[4] < 97.89667:
                    var320 = 1.7745901
                else:
                    var320 = 0.20416608
        else:
            if input[0] < 13.0:
                if input[2] < 1279.51:
                    var320 = -1.4111118
                else:
                    var320 = -0.51490355
            else:
                var320 = 2.0272431
    else:
        if input[1] < 713.0:
            if input[0] < 6.0:
                var320 = 0.62674564
            else:
                var320 = 2.704584
        else:
            if input[3] < 72.666664:
                if input[1] < 770.0:
                    var320 = 0.43346864
                else:
                    var320 = -1.2586033
            else:
                if input[3] < 83.916664:
                    var320 = 1.0401528
                else:
                    var320 = 0.010736348
    if input[8] < 49.0:
        if input[4] < 93.88143:
            if input[8] < 48.0:
                if input[4] < 69.535:
                    var321 = 0.040167835
                else:
                    var321 = -1.058431
            else:
                var321 = 3.4322937
        else:
            if input[0] < 4.0:
                if input[3] < 815.0:
                    var321 = -0.232037
                else:
                    var321 = 0.88965076
            else:
                if input[3] < 103.2:
                    var321 = 0.16030191
                else:
                    var321 = 0.8613917
    else:
        if input[8] < 50.0:
            if input[2] < 716.7:
                if input[2] < 350.58:
                    var321 = 1.5980562
                else:
                    var321 = -1.2656403
            else:
                if input[4] < 378.305:
                    var321 = -5.99858
                else:
                    var321 = -1.5739259
        else:
            if input[4] < 174.75:
                if input[4] < 144.71857:
                    var321 = -0.021370204
                else:
                    var321 = -0.89992
            else:
                if input[8] < 60.0:
                    var321 = 0.77554417
                else:
                    var321 = 0.0005089984
    if input[7] < 37.0:
        if input[7] < 36.0:
            if input[2] < 39.86:
                if input[0] < 3.0:
                    var322 = -0.13867064
                else:
                    var322 = 1.0649956
            else:
                if input[2] < 47.46:
                    var322 = -2.6823387
                else:
                    var322 = 0.008287798
        else:
            var322 = -2.0847642
    else:
        if input[1] < 1070.0:
            var322 = 1.11112
        else:
            if input[2] < 1815.6:
                if input[1] < 1086.0:
                    var322 = -0.80247957
                else:
                    var322 = 0.027036538
            else:
                var322 = 1.4017792
    if input[1] < 893.0:
        if input[1] < 697.0:
            if input[3] < 70.92308:
                if input[1] < 483.0:
                    var323 = -0.05557641
                else:
                    var323 = 0.6039787
            else:
                if input[8] < 46.0:
                    var323 = 0.12552233
                else:
                    var323 = -0.5935473
        else:
            if input[1] < 716.0:
                if input[0] < 7.0:
                    var323 = 0.6776005
                else:
                    var323 = 2.332538
            else:
                if input[3] < 65.77778:
                    var323 = -0.7479855
                else:
                    var323 = 0.22914402
    else:
        if input[1] < 934.0:
            if input[3] < 100.6:
                if input[2] < 696.14:
                    var323 = -0.14882202
                else:
                    var323 = -2.285094
            else:
                if input[4] < 205.0089:
                    var323 = 1.4008595
                else:
                    var323 = -1.64401
        else:
            if input[1] < 951.0:
                if input[0] < 6.0:
                    var323 = -0.7724457
                else:
                    var323 = 2.2364004
            else:
                if input[8] < 9.0:
                    var323 = -1.3239124
                else:
                    var323 = -0.055490732
    if input[3] < 136.14285:
        if input[3] < 126.833336:
            if input[3] < 126.0:
                if input[0] < 7.0:
                    var324 = 0.23219693
                else:
                    var324 = -0.05633535
            else:
                if input[0] < 9.0:
                    var324 = -0.90110934
                else:
                    var324 = -2.4661806
        else:
            if input[1] < 891.0:
                if input[0] < 6.0:
                    var324 = 1.3352212
                else:
                    var324 = -1.196112
            else:
                if input[1] < 1166.0:
                    var324 = 2.5786178
                else:
                    var324 = -0.11723633
    else:
        if input[3] < 252.75:
            if input[1] < 815.0:
                if input[1] < 725.0:
                    var324 = -0.41529027
                else:
                    var324 = 0.5411542
            else:
                if input[3] < 154.0:
                    var324 = -1.529144
                else:
                    var324 = -0.5850362
        else:
            if input[3] < 264.39:
                if input[0] < 3.0:
                    var324 = 2.2406654
                else:
                    var324 = 0.029375205
            else:
                if input[1] < 781.0:
                    var324 = -0.3016071
                else:
                    var324 = 0.22783081
    if input[2] < 373.98:
        if input[2] < 221.15:
            if input[1] < 66.13:
                if input[2] < 58.24:
                    var325 = -0.39762416
                else:
                    var325 = -1.4848231
            else:
                if input[3] < 30.181818:
                    var325 = 1.6349751
                else:
                    var325 = 0.09269022
        else:
            if input[1] < 255.0:
                if input[3] < 2.8:
                    var325 = 0.25162584
                else:
                    var325 = -1.2372531
            else:
                if input[3] < 72.85714:
                    var325 = 0.28725052
                else:
                    var325 = -0.7373645
    else:
        if input[2] < 413.99:
            if input[0] < 5.0:
                if input[0] < 3.0:
                    var325 = 0.015192262
                else:
                    var325 = -0.84607136
            else:
                if input[1] < 752.0:
                    var325 = 1.7910388
                else:
                    var325 = -0.48017374
        else:
            if input[4] < 36.452145:
                if input[1] < 69.0:
                    var325 = -0.12417755
                else:
                    var325 = -2.5269828
            else:
                if input[9] < 6.0:
                    var325 = 0.19136272
                else:
                    var325 = -0.012615325
    if input[4] < 101.346664:
        if input[1] < 836.0:
            if input[4] < 76.43846:
                if input[3] < 101.28571:
                    var326 = 0.09195764
                else:
                    var326 = -0.64854395
            else:
                if input[3] < 43.0:
                    var326 = -0.29983947
                else:
                    var326 = -1.6519078
        else:
            if input[2] < 696.14:
                if input[1] < 924.0:
                    var326 = 1.3425602
                else:
                    var326 = -0.7427258
            else:
                if input[4] < 66.75667:
                    var326 = -2.4306052
                else:
                    var326 = 2.5609958
    else:
        if input[1] < 885.0:
            if input[8] < 50.0:
                if input[8] < 49.0:
                    var326 = 0.13189343
                else:
                    var326 = -3.6589592
            else:
                if input[8] < 60.0:
                    var326 = 0.84463024
                else:
                    var326 = 0.20338109
        else:
            if input[3] < 85.0:
                if input[1] < 1009.0:
                    var326 = -1.8020931
                else:
                    var326 = 0.119347386
            else:
                if input[8] < 19.0:
                    var326 = -0.8762477
                else:
                    var326 = 0.18219233
    if input[4] < 153.15:
        if input[2] < 2011.28:
            if input[2] < 1013.03:
                if input[2] < 871.76:
                    var327 = 0.079731904
                else:
                    var327 = -1.0995586
            else:
                if input[1] < 1014.0:
                    var327 = 0.25830147
                else:
                    var327 = 1.5786715
        else:
            var327 = 2.7249436
    else:
        if input[3] < 128.33333:
            if input[2] < 1147.89:
                if input[4] < 369.13333:
                    var327 = 0.8227741
                else:
                    var327 = -2.0712922
            else:
                if input[3] < 126.0:
                    var327 = -0.2990217
                else:
                    var327 = -1.5969625
        else:
            if input[3] < 131.8:
                var327 = 2.0469606
            else:
                if input[4] < 169.41692:
                    var327 = 1.3397568
                else:
                    var327 = -0.038759228
    if input[1] < 1145.0:
        if input[3] < 44.11111:
            if input[0] < 14.0:
                if input[3] < 33.81818:
                    var328 = -0.059696164
                else:
                    var328 = -0.7675555
            else:
                if input[3] < 42.333332:
                    var328 = 0.7419888
                else:
                    var328 = -0.9834758
        else:
            if input[2] < 2419.86:
                if input[3] < 89.22222:
                    var328 = 0.25483674
                else:
                    var328 = -0.012148115
            else:
                if input[2] < 2447.82:
                    var328 = -1.6508579
                else:
                    var328 = -0.13907552
    else:
        if input[0] < 3.0:
            if input[1] < 1159.0:
                var328 = 0.33742067
            else:
                var328 = 1.1913376
        else:
            if input[2] < 2178.16:
                if input[2] < 555.49:
                    var328 = 0.19287227
                else:
                    var328 = -1.4569739
            else:
                if input[0] < 12.0:
                    var328 = 1.1641587
                else:
                    var328 = -0.11686402
    if input[2] < 298.68:
        if input[2] < 221.15:
            if input[6] < 4.0:
                if input[0] < 14.0:
                    var329 = -0.26998937
                else:
                    var329 = 2.073816
            else:
                if input[1] < 267.0:
                    var329 = 1.7867402
                else:
                    var329 = 0.7167075
        else:
            if input[8] < 15.0:
                if input[1] < 17.0:
                    var329 = -0.36020967
                else:
                    var329 = 1.8729385
            else:
                if input[0] < 11.0:
                    var329 = -0.9172718
                else:
                    var329 = -2.2240627
    else:
        if input[3] < 136.14285:
            if input[3] < 135.42857:
                if input[7] < 4.0:
                    var329 = 0.038811512
                else:
                    var329 = 0.51843256
            else:
                var329 = 2.8000572
        else:
            if input[3] < 141.0:
                if input[4] < 206.61363:
                    var329 = -2.4634268
                else:
                    var329 = -0.21990268
            else:
                if input[3] < 145.75:
                    var329 = 1.3405025
                else:
                    var329 = -0.10431081
    if input[2] < 2248.68:
        if input[4] < 231.4943:
            if input[4] < 219.127:
                if input[1] < 793.0:
                    var330 = -0.140525
                else:
                    var330 = 0.187042
            else:
                if input[1] < 223.0:
                    var330 = 1.2188252
                else:
                    var330 = -1.7939943
        else:
            if input[4] < 252.57286:
                if input[3] < 39.642:
                    var330 = -2.0868719
                else:
                    var330 = 1.8738693
            else:
                if input[8] < 88.0:
                    var330 = -0.110563636
                else:
                    var330 = 0.5667984
    else:
        if input[8] < 44.0:
            if input[0] < 8.0:
                if input[2] < 2385.6:
                    var330 = 1.7831446
                else:
                    var330 = -0.022755941
            else:
                if input[2] < 2359.42:
                    var330 = -1.5701569
                else:
                    var330 = -0.13487345
        else:
            if input[8] < 76.0:
                if input[1] < 17.0:
                    var330 = -1.2736969
                else:
                    var330 = 1.7878002
            else:
                if input[8] < 90.0:
                    var330 = -0.48666808
                else:
                    var330 = 0.40680066
    if input[0] < 14.0:
        if input[1] < 697.0:
            if input[2] < 2296.07:
                if input[1] < 629.0:
                    var331 = -0.15460236
                else:
                    var331 = -0.78809196
            else:
                if input[2] < 2385.6:
                    var331 = 1.3104897
                else:
                    var331 = -0.23952797
        else:
            if input[8] < 89.0:
                if input[1] < 713.0:
                    var331 = 0.9162366
                else:
                    var331 = -0.07501183
            else:
                if input[4] < 95.62:
                    var331 = 1.7651323
                else:
                    var331 = 0.10525806
    else:
        if input[1] < 597.0:
            if input[2] < 2013.45:
                if input[2] < 1358.14:
                    var331 = 0.84558547
                else:
                    var331 = -0.536499
            else:
                if input[1] < 195.73:
                    var331 = 0.4278534
                else:
                    var331 = 2.6203156
        else:
            if input[8] < 48.0:
                if input[8] < 15.0:
                    var331 = -0.86911625
                else:
                    var331 = 1.0335153
            else:
                if input[1] < 959.0:
                    var331 = 1.2787141
                else:
                    var331 = -1.2762512
    if input[3] < 61.0:
        if input[3] < 59.5:
            if input[5] < 15.0:
                if input[3] < 4.9166665:
                    var332 = -0.4724798
                else:
                    var332 = -0.00936121
            else:
                if input[2] < 958.08:
                    var332 = 0.33989057
                else:
                    var332 = -2.192438
        else:
            var332 = -1.8265532
    else:
        if input[3] < 64.57143:
            if input[8] < 78.0:
                if input[4] < 420.32:
                    var332 = 1.5824908
                else:
                    var332 = -0.3026062
            else:
                if input[8] < 93.0:
                    var332 = -1.1646988
                else:
                    var332 = 1.0866547
        else:
            if input[4] < 117.1225:
                if input[2] < 709.07:
                    var332 = 0.09467452
                else:
                    var332 = 1.1188008
            else:
                if input[3] < 79.166664:
                    var332 = -0.889468
                else:
                    var332 = 0.0053690225
    if input[2] < 863.93:
        if input[2] < 793.55:
            if input[2] < 279.75:
                if input[1] < 320.0:
                    var333 = 0.20096324
                else:
                    var333 = -0.44573507
            else:
                if input[2] < 493.0:
                    var333 = 0.45095974
                else:
                    var333 = -0.08640935
        else:
            if input[1] < 765.0:
                if input[1] < 379.0:
                    var333 = 1.148619
                else:
                    var333 = -0.44826102
            else:
                if input[0] < 11.0:
                    var333 = 2.3430848
                else:
                    var333 = 0.48004457
    else:
        if input[2] < 871.76:
            if input[3] < 141.0:
                var333 = -3.57113
            else:
                var333 = -0.8802826
        else:
            if input[1] < 753.0:
                if input[3] < 67.36364:
                    var333 = 0.002062026
                else:
                    var333 = -0.47198412
            else:
                if input[1] < 765.0:
                    var333 = 1.6278915
                else:
                    var333 = 0.037765663
    if input[8] < 52.0:
        if input[8] < 49.0:
            if input[2] < 1164.37:
                if input[2] < 493.0:
                    var334 = 0.009793983
                else:
                    var334 = -0.50681955
            else:
                if input[1] < 1012.0:
                    var334 = 0.22764699
                else:
                    var334 = -0.50518763
        else:
            if input[2] < 1059.79:
                if input[1] < 566.0:
                    var334 = 0.7038793
                else:
                    var334 = -1.423212
            else:
                if input[8] < 50.0:
                    var334 = -4.7695904
                else:
                    var334 = -0.39419678
    else:
        if input[8] < 58.0:
            if input[4] < 476.764:
                if input[8] < 55.0:
                    var334 = 0.29652318
                else:
                    var334 = 1.4061966
            else:
                if input[1] < 684.0:
                    var334 = -0.23039055
                else:
                    var334 = -1.6724875
        else:
            if input[8] < 70.0:
                if input[3] < 88.6:
                    var334 = -0.60769147
                else:
                    var334 = 0.3305089
            else:
                if input[4] < 144.71857:
                    var334 = 0.34436563
                else:
                    var334 = -0.06288287
    if input[0] < 12.0:
        if input[0] < 8.0:
            if input[2] < 1411.49:
                if input[2] < 1220.47:
                    var335 = 0.043210115
                else:
                    var335 = -0.9108489
            else:
                if input[4] < 252.57286:
                    var335 = 1.5712857
                else:
                    var335 = 0.1349405
        else:
            if input[2] < 214.08:
                if input[3] < 119.77778:
                    var335 = -1.8283814
                else:
                    var335 = 0.13136292
            else:
                if input[2] < 462.79:
                    var335 = 0.6849317
                else:
                    var335 = -0.26429495
    else:
        if input[2] < 2171.07:
            if input[2] < 2022.94:
                if input[2] < 517.54:
                    var335 = -0.2561203
                else:
                    var335 = 0.39670736
            else:
                if input[1] < 47.0:
                    var335 = 0.10864258
                else:
                    var335 = 2.9438486
        else:
            if input[8] < 69.0:
                if input[1] < 117.0:
                    var335 = 0.5048425
                else:
                    var335 = -1.0971031
            else:
                if input[1] < 713.0:
                    var335 = 0.904448
                else:
                    var335 = 0.08010341
    if input[4] < 252.57286:
        if input[4] < 245.9425:
            if input[6] < 14.0:
                if input[4] < 69.535:
                    var336 = 0.15568113
                else:
                    var336 = -0.31390652
            else:
                if input[7] < 4.0:
                    var336 = 0.06750506
                else:
                    var336 = 0.66600424
        else:
            if input[3] < 136.14285:
                if input[8] < 24.0:
                    var336 = -0.4992462
                else:
                    var336 = 3.3881326
            else:
                if input[0] < 3.0:
                    var336 = -0.71292114
                else:
                    var336 = 0.055718996
    else:
        if input[0] < 8.0:
            if input[2] < 2489.69:
                if input[1] < 152.0:
                    var336 = -0.50152844
                else:
                    var336 = 0.05053842
            else:
                var336 = 1.4722
        else:
            if input[1] < 527.0:
                if input[1] < 278.0:
                    var336 = -1.213295
                else:
                    var336 = 0.7027649
            else:
                if input[8] < 60.0:
                    var336 = -1.8003235
                else:
                    var336 = -0.30708772
    if input[2] < 1147.89:
        if input[2] < 863.93:
            if input[2] < 769.23:
                if input[3] < 24.09091:
                    var337 = -0.48930094
                else:
                    var337 = 0.0038222433
            else:
                if input[8] < 87.0:
                    var337 = 0.7474521
                else:
                    var337 = -1.5749772
        else:
            if input[2] < 910.41:
                if input[8] < 34.0:
                    var337 = -0.7034926
                else:
                    var337 = -2.2021155
            else:
                if input[1] < 896.0:
                    var337 = -0.6428259
                else:
                    var337 = 0.6770514
    else:
        if input[2] < 1210.87:
            if input[1] < 893.0:
                if input[8] < 72.0:
                    var337 = -0.39509735
                else:
                    var337 = 1.6511269
            else:
                if input[0] < 3.0:
                    var337 = 0.8518219
                else:
                    var337 = 5.4814863
        else:
            if input[1] < 885.0:
                if input[1] < 875.0:
                    var337 = 0.09055745
                else:
                    var337 = 1.8105042
            else:
                if input[1] < 1096.0:
                    var337 = -0.5503527
                else:
                    var337 = 0.29406968
    if input[1] < 447.0:
        if input[2] < 2462.26:
            if input[6] < 49.0:
                if input[4] < 109.88:
                    var338 = -0.12672898
                else:
                    var338 = 0.23240271
            else:
                if input[0] < 2.0:
                    var338 = -0.31310424
                else:
                    var338 = -1.1691663
        else:
            if input[3] < 62.272728:
                var338 = 1.8990088
            else:
                var338 = 0.49240723
    else:
        if input[1] < 586.0:
            if input[8] < 49.0:
                if input[1] < 527.0:
                    var338 = 0.9082152
                else:
                    var338 = -0.9269627
            else:
                if input[8] < 50.0:
                    var338 = -3.4516685
                else:
                    var338 = -0.59646004
        else:
            if input[1] < 606.0:
                if input[8] < 70.0:
                    var338 = 1.9812357
                else:
                    var338 = 0.0018702189
            else:
                if input[8] < 88.0:
                    var338 = -0.105575144
                else:
                    var338 = 0.3392561
    if input[1] < 1158.0:
        if input[1] < 597.0:
            if input[3] < 95.8:
                if input[3] < 92.666664:
                    var339 = -0.010285626
                else:
                    var339 = 1.310192
            else:
                if input[3] < 104.2:
                    var339 = -1.8014265
                else:
                    var339 = -0.20126
        else:
            if input[3] < 51.25:
                if input[0] < 14.0:
                    var339 = 2.567273
                else:
                    var339 = -0.54538983
            else:
                if input[3] < 60.636364:
                    var339 = -0.73132324
                else:
                    var339 = 0.17155953
    else:
        if input[4] < 69.535:
            var339 = 1.2595825
        else:
            if input[4] < 152.42166:
                if input[0] < 9.0:
                    var339 = -2.7418213
                else:
                    var339 = -0.67364657
            else:
                if input[0] < 3.0:
                    var339 = 0.77673495
                else:
                    var339 = -0.54075223
    if input[3] < 116.71429:
        if input[7] < 4.0:
            if input[3] < 95.4:
                if input[5] < 7.0:
                    var340 = -0.04011305
                else:
                    var340 = 0.2247638
            else:
                if input[4] < 149.13777:
                    var340 = 0.1388733
                else:
                    var340 = -1.5009645
        else:
            if input[8] < 65.0:
                if input[2] < 1448.55:
                    var340 = 0.24497941
                else:
                    var340 = 1.7634327
            else:
                if input[3] < 104.2:
                    var340 = 1.5798559
                else:
                    var340 = -1.0646354
    else:
        if input[3] < 141.0:
            if input[2] < 2335.55:
                if input[1] < 1145.0:
                    var340 = -0.88321704
                else:
                    var340 = 0.5079358
            else:
                if input[1] < 650.0:
                    var340 = 2.3492706
                else:
                    var340 = -0.4587036
        else:
            if input[1] < 1038.0:
                if input[1] < 981.0:
                    var340 = 0.027521675
                else:
                    var340 = 0.9860608
            else:
                if input[3] < 532.0:
                    var340 = -0.95267963
                else:
                    var340 = 0.75240594
    if input[4] < 40.83286:
        if input[3] < 21.571428:
            if input[4] < 8.236:
                if input[0] < 14.0:
                    var341 = -0.050799716
                else:
                    var341 = 2.0804107
            else:
                if input[1] < 52.0:
                    var341 = 0.00850732
                else:
                    var341 = -1.7135487
        else:
            if input[3] < 49.333332:
                if input[4] < 28.927143:
                    var341 = 0.25580403
                else:
                    var341 = 1.756456
            else:
                if input[1] < 751.0:
                    var341 = -0.8319544
                else:
                    var341 = -0.0409535
    else:
        if input[4] < 71.902:
            if input[4] < 66.75667:
                if input[1] < 32.0:
                    var341 = 1.4874085
                else:
                    var341 = 0.028952578
            else:
                if input[1] < 913.0:
                    var341 = 0.88561517
                else:
                    var341 = 2.2729065
        else:
            if input[4] < 181.24667:
                if input[4] < 144.71857:
                    var341 = 0.038529005
                else:
                    var341 = -0.44728804
            else:
                if input[3] < 169.28572:
                    var341 = 0.29725048
                else:
                    var341 = -0.11284497
    if input[8] < 32.0:
        if input[6] < 47.0:
            if input[1] < 301.0:
                if input[1] < 182.0:
                    var342 = -0.21163428
                else:
                    var342 = 0.6452458
            else:
                if input[3] < 154.0:
                    var342 = -0.5151734
                else:
                    var342 = 0.07334168
        else:
            if input[6] < 48.0:
                if input[1] < 650.0:
                    var342 = 2.2847412
                else:
                    var342 = 0.36651918
            else:
                if input[1] < 868.0:
                    var342 = -0.32768622
                else:
                    var342 = 0.8578577
    else:
        if input[1] < 1029.0:
            if input[3] < 141.0:
                if input[3] < 131.8:
                    var342 = 0.08014442
                else:
                    var342 = -1.4925549
            else:
                if input[0] < 7.0:
                    var342 = 0.32996365
                else:
                    var342 = 4.723096
        else:
            if input[1] < 1090.0:
                if input[4] < 19.542856:
                    var342 = 1.2350358
                else:
                    var342 = -1.0232838
            else:
                if input[4] < 66.75667:
                    var342 = -0.61648995
                else:
                    var342 = 0.4209226
    if input[3] < 62.0:
        if input[1] < 770.0:
            if input[0] < 12.0:
                if input[0] < 11.0:
                    var343 = -0.10892027
                else:
                    var343 = -0.72268194
            else:
                if input[4] < 37.923077:
                    var343 = -0.62779707
                else:
                    var343 = 0.34689534
        else:
            if input[8] < 7.0:
                var343 = 0.47788087
            else:
                if input[2] < 2359.42:
                    var343 = -2.4198146
                else:
                    var343 = -0.15025635
    else:
        if input[3] < 63.1:
            if input[2] < 591.44:
                if input[0] < 7.0:
                    var343 = -1.2133026
                else:
                    var343 = 1.3069458
            else:
                var343 = 1.9894125
        else:
            if input[3] < 112.44444:
                if input[7] < 4.0:
                    var343 = 0.05552432
                else:
                    var343 = 0.91410315
            else:
                if input[3] < 114.5:
                    var343 = -2.11008
                else:
                    var343 = 0.012951987
    if input[9] < 27.0:
        if input[4] < 582.37:
            if input[1] < 94.0:
                if input[3] < 31.4:
                    var344 = -0.20400468
                else:
                    var344 = -1.0726271
            else:
                if input[3] < 9.375:
                    var344 = 1.9135855
                else:
                    var344 = 0.017493287
        else:
            if input[4] < 616.0725:
                var344 = 1.8398533
            else:
                if input[1] < 247.0:
                    var344 = -0.37797546
                else:
                    var344 = 0.47511598
    else:
        if input[4] < 809.63:
            if input[8] < 26.0:
                if input[1] < 368.0:
                    var344 = 0.98078007
                else:
                    var344 = -0.38504133
            else:
                if input[3] < 109.888885:
                    var344 = 0.052560426
                else:
                    var344 = -1.6146673
        else:
            if input[9] < 36.0:
                if input[1] < 140.0:
                    var344 = -0.8400055
                else:
                    var344 = 0.7558086
            else:
                if input[8] < 42.0:
                    var344 = 0.08007188
                else:
                    var344 = -0.54401976
    if input[9] < 25.0:
        if input[4] < 582.37:
            if input[1] < 862.0:
                if input[1] < 852.0:
                    var345 = 0.010751617
                else:
                    var345 = 1.153686
            else:
                if input[3] < 80.545456:
                    var345 = -1.2931479
                else:
                    var345 = -0.045658644
        else:
            if input[4] < 616.0725:
                if input[1] < 182.0:
                    var345 = 0.57590336
                else:
                    var345 = 1.8607901
            else:
                if input[1] < 508.0:
                    var345 = 0.4523173
                else:
                    var345 = 0.043707278
    else:
        if input[8] < 26.0:
            if input[1] < 368.0:
                if input[8] < 9.0:
                    var345 = 0.26143035
                else:
                    var345 = 0.9515424
            else:
                if input[1] < 795.0:
                    var345 = -0.4060204
                else:
                    var345 = 0.630659
        else:
            if input[4] < 809.63:
                if input[9] < 26.0:
                    var345 = -0.20838013
                else:
                    var345 = -1.200686
            else:
                if input[4] < 1143.58:
                    var345 = 0.13227683
                else:
                    var345 = -0.5022035
    if input[8] < 52.0:
        if input[8] < 49.0:
            if input[8] < 48.0:
                if input[4] < 104.1175:
                    var346 = -0.41646075
                else:
                    var346 = 0.022560922
            else:
                if input[1] < 643.0:
                    var346 = -0.9892456
                else:
                    var346 = 2.2157898
        else:
            if input[2] < 1059.79:
                if input[1] < 566.0:
                    var346 = 0.7209692
                else:
                    var346 = -0.878066
            else:
                if input[8] < 50.0:
                    var346 = -5.1594367
                else:
                    var346 = 0.19698748
    else:
        if input[7] < 2.0:
            if input[0] < 3.0:
                if input[2] < 17.43:
                    var346 = -0.34768066
                else:
                    var346 = -1.9269571
            else:
                if input[0] < 5.0:
                    var346 = 0.81179494
                else:
                    var346 = -0.24270247
        else:
            if input[7] < 3.0:
                if input[1] < 981.0:
                    var346 = 0.66498476
                else:
                    var346 = 3.2302003
            else:
                if input[4] < 125.935:
                    var346 = 0.68120146
                else:
                    var346 = -0.1551565
    if input[3] < 989.0:
        if input[8] < 76.0:
            if input[8] < 72.0:
                if input[1] < 182.0:
                    var347 = -0.38730696
                else:
                    var347 = 0.03522149
            else:
                if input[1] < 1006.0:
                    var347 = 0.26310506
                else:
                    var347 = 2.2726233
        else:
            if input[1] < 831.0:
                if input[3] < 73.55556:
                    var347 = -0.26160955
                else:
                    var347 = 0.22866929
            else:
                if input[3] < 71.4:
                    var347 = 1.5147934
                else:
                    var347 = -0.684565
    else:
        if input[8] < 1.0:
            var347 = 0.04436035
        else:
            if input[4] < 396.49:
                var347 = 0.19083405
            else:
                var347 = 1.0726172
    if input[1] < 1070.0:
        if input[1] < 1062.0:
            if input[0] < 11.0:
                if input[8] < 48.0:
                    var348 = 0.22449131
                else:
                    var348 = -0.0391951
            else:
                if input[8] < 39.0:
                    var348 = -0.67489195
                else:
                    var348 = 0.1691684
        else:
            if input[2] < 2013.45:
                var348 = 1.9712433
            else:
                var348 = -0.09333191
    else:
        if input[1] < 1086.0:
            if input[0] < 11.0:
                if input[4] < 121.096664:
                    var348 = -1.9917725
                else:
                    var348 = -0.670794
            else:
                if input[1] < 1075.0:
                    var348 = 0.8410126
                else:
                    var348 = 0.03538615
        else:
            if input[2] < 1460.21:
                if input[4] < 25.788:
                    var348 = -0.6520826
                else:
                    var348 = 0.5432499
            else:
                if input[0] < 3.0:
                    var348 = 0.7276941
                else:
                    var348 = -0.6910493
    if input[1] < 17.0:
        if input[0] < 5.0:
            if input[0] < 3.0:
                if input[0] < 2.0:
                    var349 = -0.083401494
                else:
                    var349 = -0.3117222
            else:
                if input[1] < 9.0:
                    var349 = -0.0851944
                else:
                    var349 = 0.9567205
        else:
            if input[4] < 85.848:
                if input[2] < 268.91:
                    var349 = -0.84040415
                else:
                    var349 = 0.37634277
            else:
                if input[2] < 1059.79:
                    var349 = -0.413973
                else:
                    var349 = -1.5204517
    else:
        if input[4] < 21.13:
            if input[2] < 159.26:
                if input[3] < 115.75:
                    var349 = 0.23247993
                else:
                    var349 = -0.6230799
            else:
                if input[4] < 16.933332:
                    var349 = -0.05067546
                else:
                    var349 = 2.3354127
        else:
            if input[4] < 28.927143:
                if input[0] < 3.0:
                    var349 = 0.8760411
                else:
                    var349 = -0.8334481
            else:
                if input[4] < 34.532856:
                    var349 = 0.9660078
                else:
                    var349 = 0.020520894
    if input[3] < 116.71429:
        if input[3] < 100.6:
            if input[3] < 95.8:
                if input[3] < 37.857143:
                    var350 = -0.11435405
                else:
                    var350 = 0.1283434
            else:
                if input[0] < 10.0:
                    var350 = -1.5737747
                else:
                    var350 = 0.06008301
        else:
            if input[6] < 10.0:
                if input[4] < 13.319285:
                    var350 = 1.7572354
                else:
                    var350 = -0.89867204
            else:
                if input[6] < 40.0:
                    var350 = 1.43936
                else:
                    var350 = 0.22507374
    else:
        if input[4] < 8.715:
            var350 = -2.110675
        else:
            if input[3] < 142.5:
                if input[4] < 24.540909:
                    var350 = 1.2938473
                else:
                    var350 = -0.63005936
            else:
                if input[0] < 7.0:
                    var350 = -0.066957556
                else:
                    var350 = 0.7492947
    var351 = var295 + var296 + var297 + var298 + var299 + var300 + var301 + var302 + var303 + var304 + var305 + var306 + var307 + var308 + var309 + var310 + var311 + var312 + var313 + var314 + var315 + var316 + var317 + var318 + var319 + var320 + var321 + var322 + var323 + var324 + var325 + var326 + var327 + var328 + var329 + var330 + var331 + var332 + var333 + var334 + var335 + var336 + var337 + var338 + var339 + var340 + var341 + var342 + var343 + var344 + var345 + var346 + var347 + var348 + var349 + var350
    if input[3] < 61.0:
        if input[3] < 57.642857:
            if input[7] < 2.0:
                if input[4] < 8.236:
                    var352 = 0.8017871
                else:
                    var352 = -0.22576283
            else:
                if input[4] < 172.25874:
                    var352 = -0.2842231
                else:
                    var352 = 1.6958697
        else:
            if input[4] < 203.704:
                if input[4] < 138.36539:
                    var352 = -0.7265756
                else:
                    var352 = -1.7707363
            else:
                if input[1] < 247.0:
                    var352 = 0.7303711
                else:
                    var352 = 0.07415568
    else:
        if input[3] < 63.1:
            if input[1] < 690.0:
                if input[4] < 62.18308:
                    var352 = 2.3500733
                else:
                    var352 = 0.9415432
            else:
                var352 = -0.32949677
        else:
            if input[4] < 219.127:
                if input[1] < 697.0:
                    var352 = -0.22379711
                else:
                    var352 = 0.28550223
            else:
                if input[4] < 231.4943:
                    var352 = -1.309714
                else:
                    var352 = -0.00093192887
    if input[3] < 70.25:
        if input[3] < 59.5:
            if input[2] < 1249.41:
                if input[4] < 197.51666:
                    var353 = -0.088665165
                else:
                    var353 = -2.1184263
            else:
                if input[8] < 70.0:
                    var353 = 0.021824248
                else:
                    var353 = 0.85800475
        else:
            if input[4] < 70.6:
                if input[8] < 78.0:
                    var353 = 2.344111
                else:
                    var353 = 0.18002686
            else:
                if input[0] < 11.0:
                    var353 = -0.25336567
                else:
                    var353 = 0.8159507
    else:
        if input[3] < 72.666664:
            if input[2] < 716.7:
                if input[0] < 11.0:
                    var353 = 1.1169678
                else:
                    var353 = -0.61616516
            else:
                if input[8] < 23.0:
                    var353 = -0.7212484
                else:
                    var353 = -1.8986357
        else:
            if input[3] < 73.55556:
                if input[2] < 517.54:
                    var353 = -0.7314588
                else:
                    var353 = 3.086322
            else:
                if input[8] < 47.0:
                    var353 = 0.04651774
                else:
                    var353 = -0.25325784
    if input[1] < 1162.0:
        if input[1] < 1158.0:
            if input[1] < 1153.0:
                if input[1] < 1145.0:
                    var354 = 0.011556959
                else:
                    var354 = -1.5716345
            else:
                if input[0] < 3.0:
                    var354 = 0.24516602
                else:
                    var354 = 1.67512
        else:
            if input[8] < 28.0:
                var354 = -0.02935791
            else:
                var354 = -1.3186203
    else:
        if input[4] < 95.62:
            if input[4] < 1.9266666:
                var354 = 0.07673035
            else:
                var354 = 1.5841583
        else:
            if input[2] < 1639.17:
                if input[7] < 16.0:
                    var354 = -1.1641922
                else:
                    var354 = 0.8081812
            else:
                if input[2] < 1901.83:
                    var354 = 1.8143845
                else:
                    var354 = 0.17046814
    if input[5] < 21.0:
        if input[5] < 12.0:
            if input[0] < 12.0:
                if input[0] < 7.0:
                    var355 = -0.03361074
                else:
                    var355 = -0.4245401
            else:
                if input[4] < 179.72:
                    var355 = 0.46165013
                else:
                    var355 = -0.78379214
        else:
            if input[3] < 51.25:
                if input[3] < 47.2:
                    var355 = -0.14225769
                else:
                    var355 = 2.3979688
            else:
                if input[0] < 12.0:
                    var355 = 0.21233402
                else:
                    var355 = -0.5115737
    else:
        if input[3] < 118.7:
            if input[8] < 44.0:
                if input[2] < 1084.16:
                    var355 = 1.9683602
                else:
                    var355 = -0.48151246
            else:
                if input[4] < 167.80833:
                    var355 = -1.0197588
                else:
                    var355 = 0.7687645
        else:
            if input[3] < 399.0:
                if input[8] < 36.0:
                    var355 = -1.1566044
                else:
                    var355 = -0.4487353
            else:
                if input[3] < 1068.0:
                    var355 = 0.6489399
                else:
                    var355 = -0.12060525
    if input[0] < 8.0:
        if input[3] < 136.14285:
            if input[5] < 7.0:
                if input[8] < 93.0:
                    var356 = 0.059564043
                else:
                    var356 = -0.76904166
            else:
                if input[2] < 314.81:
                    var356 = -0.46797386
                else:
                    var356 = 0.881775
        else:
            if input[3] < 141.0:
                if input[1] < 836.0:
                    var356 = -0.0075546266
                else:
                    var356 = -2.3327653
            else:
                if input[0] < 7.0:
                    var356 = -0.040514227
                else:
                    var356 = 0.717303
    else:
        if input[9] < 6.0:
            if input[9] < 5.0:
                if input[3] < 115.75:
                    var356 = -0.023357121
                else:
                    var356 = -1.2245749
            else:
                if input[8] < 5.0:
                    var356 = -1.1379175
                else:
                    var356 = 0.91552687
        else:
            if input[8] < 91.0:
                if input[8] < 86.0:
                    var356 = -0.30265424
                else:
                    var356 = 0.80289745
            else:
                if input[8] < 98.0:
                    var356 = -1.2562699
                else:
                    var356 = -0.11395264
    if input[4] < 21.13:
        if input[4] < 20.27:
            if input[1] < 85.0:
                if input[2] < 58.24:
                    var357 = -0.12272811
                else:
                    var357 = -1.190533
            else:
                if input[8] < 16.0:
                    var357 = -0.9965172
                else:
                    var357 = 0.68716747
        else:
            var357 = 2.3092186
    else:
        if input[4] < 26.626667:
            if input[4] < 24.540909:
                if input[8] < 13.0:
                    var357 = -1.6643082
                else:
                    var357 = 0.34236577
            else:
                if input[0] < 12.0:
                    var357 = -1.8854208
                else:
                    var357 = -0.17250367
        else:
            if input[1] < 1086.0:
                if input[1] < 1029.0:
                    var357 = -0.014509766
                else:
                    var357 = -0.6605894
            else:
                if input[4] < 208.32:
                    var357 = 0.9237974
                else:
                    var357 = -0.11227578
    if input[0] < 12.0:
        if input[4] < 189.40462:
            if input[1] < 697.0:
                if input[2] < 954.02:
                    var358 = -0.057353716
                else:
                    var358 = -0.88848966
            else:
                if input[2] < 999.45:
                    var358 = -0.2493023
                else:
                    var358 = 0.8781638
        else:
            if input[4] < 193.4:
                var358 = 1.9913788
            else:
                if input[1] < 1116.0:
                    var358 = 0.08509634
                else:
                    var358 = -0.5504968
    else:
        if input[2] < 517.54:
            if input[2] < 271.93:
                if input[1] < 1080.0:
                    var358 = 0.6909062
                else:
                    var358 = -0.9468567
            else:
                if input[8] < 3.0:
                    var358 = 0.96168107
                else:
                    var358 = -1.713431
        else:
            if input[1] < 713.0:
                if input[1] < 175.0:
                    var358 = 0.11373265
                else:
                    var358 = 1.0154363
            else:
                if input[1] < 987.0:
                    var358 = -0.69390076
                else:
                    var358 = 0.78229326
    if input[4] < 135.67334:
        if input[3] < 145.75:
            if input[5] < 12.0:
                if input[3] < 47.909092:
                    var359 = 0.036462676
                else:
                    var359 = -0.6796515
            else:
                if input[8] < 90.0:
                    var359 = 0.05672347
                else:
                    var359 = 1.1515508
        else:
            if input[3] < 158.8:
                if input[2] < 579.29:
                    var359 = -1.049342
                else:
                    var359 = -3.1627624
            else:
                if input[8] < 47.0:
                    var359 = 0.39504978
                else:
                    var359 = -0.58743346
    else:
        if input[4] < 138.36539:
            if input[8] < 80.0:
                if input[8] < 2.0:
                    var359 = -0.19884644
                else:
                    var359 = 2.4944408
            else:
                if input[0] < 7.0:
                    var359 = -1.4957322
                else:
                    var359 = -0.2608826
        else:
            if input[4] < 142.11667:
                if input[3] < 63.1:
                    var359 = 0.044457756
                else:
                    var359 = -2.6664124
            else:
                if input[4] < 142.3689:
                    var359 = 2.0772817
                else:
                    var359 = 0.018263122
    if input[7] < 42.0:
        if input[4] < 1143.58:
            if input[4] < 356.10333:
                if input[2] < 2273.6:
                    var360 = -0.025450503
                else:
                    var360 = -0.6088842
            else:
                if input[4] < 476.764:
                    var360 = 0.5866715
                else:
                    var360 = 0.028638804
        else:
            if input[2] < 1300.05:
                var360 = -1.5629871
            else:
                if input[7] < 34.0:
                    var360 = -0.48934937
                else:
                    var360 = 0.50164896
    else:
        if input[1] < 1113.0:
            if input[1] < 1062.0:
                var360 = 0.5240845
            else:
                var360 = 1.4482483
        else:
            if input[2] < 863.93:
                var360 = -0.6478302
            else:
                var360 = 0.37806806
    if input[0] < 13.0:
        if input[4] < 118.291664:
            if input[4] < 101.346664:
                if input[2] < 871.76:
                    var361 = 0.13124864
                else:
                    var361 = -0.89833736
            else:
                if input[1] < 958.0:
                    var361 = 0.8457209
                else:
                    var361 = -1.8457612
        else:
            if input[4] < 125.935:
                if input[0] < 12.0:
                    var361 = -1.6532214
                else:
                    var361 = 0.12145386
            else:
                if input[2] < 910.41:
                    var361 = -0.25353917
                else:
                    var361 = 0.033621266
    else:
        if input[1] < 36.0:
            if input[1] < 14.0:
                var361 = -0.16051637
            else:
                var361 = 1.7148316
        else:
            if input[8] < 70.0:
                if input[2] < 517.54:
                    var361 = -2.0470655
                else:
                    var361 = -0.3455957
            else:
                if input[8] < 92.0:
                    var361 = 0.82236224
                else:
                    var361 = -0.88837546
    if input[3] < 33.81818:
        if input[3] < 33.1175:
            if input[3] < 32.333332:
                if input[2] < 749.56:
                    var362 = -0.15703668
                else:
                    var362 = 0.3592661
            else:
                var362 = -1.7223959
        else:
            if input[1] < 265.0:
                var362 = 0.21272431
            else:
                var362 = 2.1710563
    else:
        if input[3] < 37.857143:
            if input[1] < 362.0:
                if input[2] < 2072.39:
                    var362 = 0.088898085
                else:
                    var362 = -1.7702637
            else:
                var362 = -1.4492413
        else:
            if input[3] < 38.95:
                if input[0] < 9.0:
                    var362 = 0.31434327
                else:
                    var362 = 1.7507187
            else:
                if input[1] < 125.0:
                    var362 = -0.73868054
                else:
                    var362 = -0.014114049
    if input[1] < 512.0:
        if input[1] < 482.0:
            if input[0] < 11.0:
                if input[0] < 4.0:
                    var363 = -0.19160384
                else:
                    var363 = 0.31497404
            else:
                if input[8] < 28.0:
                    var363 = 0.25468308
                else:
                    var363 = -0.5330863
        else:
            if input[2] < 78.33:
                var363 = -0.2892619
            else:
                if input[1] < 508.0:
                    var363 = 2.1929283
                else:
                    var363 = 0.51671547
    else:
        if input[1] < 522.0:
            if input[2] < 1477.23:
                if input[8] < 26.0:
                    var363 = 2.1705942
                else:
                    var363 = -0.6808447
            else:
                var363 = -6.850757
        else:
            if input[1] < 532.0:
                if input[2] < 137.84:
                    var363 = -0.5041687
                else:
                    var363 = 2.0670373
            else:
                if input[1] < 586.0:
                    var363 = -0.7525012
                else:
                    var363 = -0.054121632
    if input[8] < 13.0:
        if input[1] < 885.0:
            if input[8] < 10.0:
                if input[2] < 852.7:
                    var364 = 0.71276873
                else:
                    var364 = -0.38980103
            else:
                if input[2] < 1429.04:
                    var364 = -1.7114115
                else:
                    var364 = 0.43684432
        else:
            if input[4] < 199.196:
                if input[0] < 4.0:
                    var364 = -0.07760417
                else:
                    var364 = -1.5120205
            else:
                if input[4] < 216.87273:
                    var364 = 1.7122742
                else:
                    var364 = -0.5295786
    else:
        if input[8] < 49.0:
            if input[3] < 99.545456:
                if input[8] < 19.0:
                    var364 = 0.5095958
                else:
                    var364 = -0.16423982
            else:
                if input[3] < 130.2:
                    var364 = 1.2272881
                else:
                    var364 = 0.10561948
        else:
            if input[8] < 50.0:
                if input[2] < 568.58:
                    var364 = 0.8079282
                else:
                    var364 = -3.6976025
            else:
                if input[3] < 11.222222:
                    var364 = 0.4945396
                else:
                    var364 = -0.09015653
    if input[0] < 8.0:
        if input[2] < 2489.69:
            if input[3] < 36.857143:
                if input[3] < 31.4:
                    var365 = 0.08318588
                else:
                    var365 = -1.5716658
            else:
                if input[0] < 7.0:
                    var365 = 0.09040237
                else:
                    var365 = 0.58977526
        else:
            var365 = 1.2928574
    else:
        if input[4] < 302.982:
            if input[8] < 12.0:
                if input[4] < 61.13727:
                    var365 = 0.61258674
                else:
                    var365 = -0.9255422
            else:
                if input[8] < 25.0:
                    var365 = 0.6818449
                else:
                    var365 = -0.12679505
        else:
            var365 = -1.7802231
    if input[8] < 51.0:
        if input[8] < 48.0:
            if input[0] < 11.0:
                if input[1] < 1038.0:
                    var366 = 0.1444849
                else:
                    var366 = -0.3496953
            else:
                if input[1] < 770.0:
                    var366 = -0.020732772
                else:
                    var366 = -0.8520832
        else:
            if input[0] < 4.0:
                if input[1] < 265.0:
                    var366 = 1.3553114
                else:
                    var366 = -0.30309042
            else:
                if input[9] < 15.0:
                    var366 = -1.2877059
                else:
                    var366 = -6.589307
    else:
        if input[6] < 42.0:
            if input[9] < 9.0:
                if input[1] < 1020.0:
                    var366 = -0.10855027
                else:
                    var366 = 0.5451873
            else:
                if input[3] < 53.555557:
                    var366 = 1.5921673
                else:
                    var366 = 0.13082975
        else:
            if input[8] < 57.0:
                if input[8] < 54.0:
                    var366 = -0.29573485
                else:
                    var366 = 2.2703116
            else:
                if input[8] < 60.0:
                    var366 = -1.6942505
                else:
                    var366 = 0.41458613
    if input[1] < 1185.0:
        if input[8] < 87.0:
            if input[8] < 84.0:
                if input[8] < 83.0:
                    var367 = -0.060853582
                else:
                    var367 = 0.88738585
            else:
                if input[1] < 32.0:
                    var367 = 0.98451006
                else:
                    var367 = -0.93869275
        else:
            if input[2] < 1346.21:
                if input[1] < 625.0:
                    var367 = -0.06862297
                else:
                    var367 = 1.7315165
            else:
                if input[2] < 1916.03:
                    var367 = -0.86718446
                else:
                    var367 = -0.10105433
    else:
        if input[2] < 477.17:
            if input[1] < 1199.0:
                if input[0] < 7.0:
                    var367 = -0.06542053
                else:
                    var367 = -1.3023713
            else:
                if input[0] < 4.0:
                    var367 = 0.050050355
                else:
                    var367 = 0.18805848
        else:
            if input[0] < 11.0:
                if input[2] < 1990.0:
                    var367 = 1.6154515
                else:
                    var367 = 0.5737712
            else:
                if input[1] < 1192.0:
                    var367 = 0.10447388
                else:
                    var367 = 0.45194703
    if input[8] < 81.0:
        if input[8] < 74.0:
            if input[3] < 44.11111:
                if input[8] < 67.0:
                    var368 = -0.09425057
                else:
                    var368 = -0.960615
            else:
                if input[6] < 11.0:
                    var368 = 0.33572793
                else:
                    var368 = -0.001590513
        else:
            if input[3] < 76.333336:
                if input[4] < 64.46167:
                    var368 = -0.52284235
                else:
                    var368 = 1.5815322
            else:
                if input[1] < 1136.0:
                    var368 = -0.42256784
                else:
                    var368 = 1.9828869
    else:
        if input[1] < 778.0:
            if input[1] < 544.0:
                if input[1] < 52.0:
                    var368 = 0.8307274
                else:
                    var368 = -0.35462618
            else:
                if input[6] < 31.0:
                    var368 = 1.1242325
                else:
                    var368 = 0.05217507
        else:
            if input[0] < 8.0:
                if input[4] < 145.96428:
                    var368 = -2.3195822
                else:
                    var368 = -0.8696396
            else:
                if input[8] < 91.0:
                    var368 = 0.19350907
                else:
                    var368 = -0.7849933
    if input[8] < 8.0:
        if input[0] < 8.0:
            if input[5] < 19.0:
                if input[0] < 7.0:
                    var369 = -0.12722878
                else:
                    var369 = -0.881072
            else:
                if input[8] < 5.0:
                    var369 = 1.2029699
                else:
                    var369 = -0.9764099
        else:
            if input[0] < 14.0:
                if input[8] < 3.0:
                    var369 = -0.3240436
                else:
                    var369 = -1.5539504
            else:
                if input[8] < 6.0:
                    var369 = -0.22667645
                else:
                    var369 = 1.4241008
    else:
        if input[8] < 10.0:
            if input[4] < 205.92818:
                if input[0] < 3.0:
                    var369 = 0.053109743
                else:
                    var369 = 2.2283251
            else:
                if input[0] < 5.0:
                    var369 = -0.5335978
                else:
                    var369 = -1.463559
        else:
            if input[8] < 12.0:
                if input[2] < 2195.67:
                    var369 = -1.1475705
                else:
                    var369 = 0.011624145
            else:
                if input[8] < 14.0:
                    var369 = 0.69163555
                else:
                    var369 = 0.0124929035
    if input[2] < 863.93:
        if input[1] < 774.0:
            if input[1] < 482.0:
                if input[1] < 447.0:
                    var370 = 0.17761324
                else:
                    var370 = -0.62531567
            else:
                if input[3] < 51.25:
                    var370 = 2.833982
                else:
                    var370 = 0.38440523
        else:
            if input[1] < 782.17:
                var370 = -2.4469192
            else:
                if input[4] < 86.75:
                    var370 = -0.41531044
                else:
                    var370 = 0.4645651
    else:
        if input[2] < 910.41:
            if input[2] < 865.92:
                if input[0] < 4.0:
                    var370 = -0.81411135
                else:
                    var370 = -2.9797058
            else:
                if input[1] < 1053.0:
                    var370 = -1.332542
                else:
                    var370 = 1.6615937
        else:
            if input[0] < 8.0:
                if input[2] < 999.45:
                    var370 = 1.117854
                else:
                    var370 = 0.036041006
            else:
                if input[2] < 1013.03:
                    var370 = -0.95992404
                else:
                    var370 = -0.08534963
    if input[1] < 597.0:
        if input[1] < 560.0:
            if input[1] < 544.0:
                if input[3] < 10.0:
                    var371 = 0.25427768
                else:
                    var371 = -0.13242932
            else:
                if input[2] < 124.65:
                    var371 = 0.042172242
                else:
                    var371 = 1.3113167
        else:
            if input[4] < 173.92125:
                if input[3] < 42.333332:
                    var371 = 0.22337036
                else:
                    var371 = -2.1037421
            else:
                if input[1] < 586.0:
                    var371 = -0.1644567
                else:
                    var371 = 0.8595256
    else:
        if input[3] < 51.25:
            if input[3] < 47.2:
                if input[1] < 616.0:
                    var371 = -0.7037598
                else:
                    var371 = 0.74533695
            else:
                if input[3] < 47.909092:
                    var371 = 0.64651185
                else:
                    var371 = 2.3738236
        else:
            if input[4] < 117.1225:
                if input[2] < 709.07:
                    var371 = 0.048835143
                else:
                    var371 = 0.93425655
            else:
                if input[4] < 121.096664:
                    var371 = -1.7947928
                else:
                    var371 = 0.017244702
    if input[1] < 1162.0:
        if input[4] < 271.90875:
            if input[4] < 40.83286:
                if input[2] < 477.17:
                    var372 = -0.23691002
                else:
                    var372 = -2.564492
            else:
                if input[4] < 231.4943:
                    var372 = 0.028446633
                else:
                    var372 = 0.45888337
        else:
            if input[1] < 140.0:
                if input[1] < 57.0:
                    var372 = 0.19236992
                else:
                    var372 = -1.5467691
            else:
                if input[8] < 55.0:
                    var372 = -0.34071743
                else:
                    var372 = 0.09914255
    else:
        if input[0] < 5.0:
            if input[4] < 544.2833:
                if input[2] < 1013.03:
                    var372 = 0.24764787
                else:
                    var372 = -1.8489045
            else:
                var372 = 1.0158234
        else:
            if input[4] < 190.612:
                if input[4] < 95.62:
                    var372 = 1.2009624
                else:
                    var372 = -0.35802716
            else:
                if input[2] < 1990.0:
                    var372 = 1.7434987
                else:
                    var372 = 0.36618653
    if input[4] < 66.496155:
        if input[3] < 70.25:
            if input[1] < 362.0:
                if input[8] < 28.0:
                    var373 = 1.1059353
                else:
                    var373 = -0.05385859
            else:
                if input[8] < 73.0:
                    var373 = 2.242322
                else:
                    var373 = 0.24466553
        else:
            if input[3] < 81.2:
                if input[6] < 3.0:
                    var373 = 0.8117694
                else:
                    var373 = -1.4134482
            else:
                if input[8] < 13.0:
                    var373 = -0.5865944
                else:
                    var373 = 0.20325501
    else:
        if input[4] < 66.75667:
            if input[1] < 104.0:
                var373 = 0.26811218
            else:
                var373 = -2.6283891
        else:
            if input[2] < 709.07:
                if input[3] < 169.28572:
                    var373 = -0.6176632
                else:
                    var373 = 0.10188346
            else:
                if input[2] < 716.7:
                    var373 = 2.0730805
                else:
                    var373 = 0.0664897
    if input[8] < 92.0:
        if input[8] < 90.0:
            if input[3] < 188.4:
                if input[3] < 154.0:
                    var374 = 0.07327688
                else:
                    var374 = 0.79650867
            else:
                if input[3] < 199.66667:
                    var374 = -1.2784264
                else:
                    var374 = -0.021514824
        else:
            if input[6] < 21.0:
                if input[3] < 183.8:
                    var374 = 2.3456929
                else:
                    var374 = 0.2411784
            else:
                if input[1] < 577.0:
                    var374 = 0.17346923
                else:
                    var374 = -1.0657943
    else:
        if input[4] < 8.236:
            if input[0] < 5.0:
                if input[0] < 4.0:
                    var374 = 0.15982667
                else:
                    var374 = -0.5132187
            else:
                var374 = 2.3855815
        else:
            if input[3] < 128.33333:
                if input[6] < 22.0:
                    var374 = -0.9109953
                else:
                    var374 = -0.3107906
            else:
                if input[6] < 10.0:
                    var374 = -0.38285053
                else:
                    var374 = 0.8191379
    if input[2] < 373.98:
        if input[4] < 21.13:
            if input[4] < 16.933332:
                if input[0] < 14.0:
                    var375 = -0.18145405
                else:
                    var375 = 1.444455
            else:
                if input[0] < 14.0:
                    var375 = 1.2331657
                else:
                    var375 = -1.5020081
        else:
            if input[0] < 8.0:
                if input[2] < 106.86:
                    var375 = 0.47465393
                else:
                    var375 = -0.7775989
            else:
                if input[4] < 34.532856:
                    var375 = -0.23723848
                else:
                    var375 = 1.4772027
    else:
        if input[4] < 36.452145:
            if input[0] < 13.0:
                var375 = -0.1772873
            else:
                var375 = -2.1915262
        else:
            if input[2] < 1210.87:
                if input[2] < 1171.99:
                    var375 = 0.10851083
                else:
                    var375 = 2.022737
            else:
                if input[2] < 1220.47:
                    var375 = -1.0740753
                else:
                    var375 = -0.03301717
    if input[7] < 4.0:
        if input[1] < 862.0:
            if input[4] < 133.09222:
                if input[4] < 64.46167:
                    var376 = 0.14323552
                else:
                    var376 = -0.4766027
            else:
                if input[4] < 138.36539:
                    var376 = 1.6023263
                else:
                    var376 = 0.06364616
        else:
            if input[1] < 1020.0:
                if input[3] < 77.23077:
                    var376 = -0.18582255
                else:
                    var376 = -1.3047464
            else:
                if input[8] < 70.0:
                    var376 = -0.19114058
                else:
                    var376 = 1.0358343
    else:
        if input[0] < 7.0:
            if input[8] < 19.0:
                if input[0] < 6.0:
                    var376 = -0.25574806
                else:
                    var376 = -1.8193232
            else:
                if input[3] < 141.0:
                    var376 = -0.32162538
                else:
                    var376 = 0.21567948
        else:
            if input[2] < 587.38:
                if input[2] < 555.49:
                    var376 = 0.21695189
                else:
                    var376 = -3.761263
            else:
                if input[1] < 1029.0:
                    var376 = 1.5133439
                else:
                    var376 = 0.017876817
    if input[0] < 8.0:
        if input[2] < 1690.22:
            if input[1] < 566.0:
                if input[1] < 403.0:
                    var377 = 0.035258915
                else:
                    var377 = 0.83963984
            else:
                if input[0] < 7.0:
                    var377 = -0.3141658
                else:
                    var377 = 0.6329687
        else:
            if input[2] < 1807.71:
                if input[1] < 483.0:
                    var377 = 0.4822231
                else:
                    var377 = 2.230611
            else:
                if input[1] < 259.96:
                    var377 = -0.51399106
                else:
                    var377 = 0.36122724
    else:
        if input[2] < 47.46:
            var377 = -2.216662
        else:
            if input[9] < 12.0:
                if input[8] < 8.0:
                    var377 = -0.5414962
                else:
                    var377 = 0.011182508
            else:
                var377 = -1.6873093
    if input[4] < 76.43846:
        if input[2] < 910.41:
            if input[0] < 4.0:
                if input[2] < 21.17:
                    var378 = 0.116611265
                else:
                    var378 = 1.082522
            else:
                if input[0] < 6.0:
                    var378 = -0.9187895
                else:
                    var378 = 0.14399864
        else:
            if input[4] < 69.535:
                if input[1] < 52.0:
                    var378 = -0.10154114
                else:
                    var378 = -1.2338685
            else:
                if input[8] < 42.0:
                    var378 = 0.8706833
                else:
                    var378 = 2.7389467
    else:
        if input[4] < 85.848:
            if input[1] < 353.0:
                if input[0] < 11.0:
                    var378 = 1.2343663
                else:
                    var378 = -0.58118165
            else:
                if input[0] < 12.0:
                    var378 = -2.0919223
                else:
                    var378 = 0.5441101
        else:
            if input[4] < 86.75:
                if input[0] < 6.0:
                    var378 = -0.8990733
                else:
                    var378 = 2.855593
            else:
                if input[8] < 64.0:
                    var378 = 0.080825105
                else:
                    var378 = -0.12993014
    if input[1] < 389.0:
        if input[2] < 2077.07:
            if input[8] < 15.0:
                if input[1] < 296.0:
                    var379 = 0.64638704
                else:
                    var379 = -0.37247315
            else:
                if input[2] < 1897.29:
                    var379 = -0.01191806
                else:
                    var379 = -1.0085907
        else:
            if input[1] < 344.0:
                if input[8] < 10.0:
                    var379 = -0.8223409
                else:
                    var379 = 0.3978246
            else:
                var379 = 2.268136
    else:
        if input[4] < 24.540909:
            if input[8] < 16.0:
                if input[0] < 12.0:
                    var379 = -1.3387512
                else:
                    var379 = -0.30008546
            else:
                if input[2] < 159.26:
                    var379 = 0.20844455
                else:
                    var379 = 1.7808493
        else:
            if input[4] < 36.452145:
                if input[8] < 25.0:
                    var379 = 0.7446635
                else:
                    var379 = -1.4489022
            else:
                if input[1] < 586.0:
                    var379 = -0.35553798
                else:
                    var379 = -0.06809437
    if input[1] < 389.0:
        if input[5] < 7.0:
            if input[8] < 92.0:
                if input[8] < 71.0:
                    var380 = -0.047454085
                else:
                    var380 = 0.49700928
            else:
                if input[4] < 8.236:
                    var380 = 1.3343685
                else:
                    var380 = -0.75405824
        else:
            if input[2] < 2049.71:
                if input[2] < 449.83:
                    var380 = 1.6258763
                else:
                    var380 = -0.26490998
            else:
                var380 = 2.0386302
    else:
        if input[4] < 5.848889:
            if input[0] < 5.0:
                var380 = -0.4910431
            else:
                if input[0] < 12.0:
                    var380 = 2.225537
                else:
                    var380 = 0.24934895
        else:
            if input[5] < 19.0:
                if input[1] < 896.0:
                    var380 = -0.16333482
                else:
                    var380 = -0.7692617
            else:
                if input[1] < 959.0:
                    var380 = 1.0176167
                else:
                    var380 = 0.0006730461
    if input[7] < 12.0:
        if input[3] < 252.75:
            if input[4] < 309.91626:
                if input[3] < 210.0:
                    var381 = 0.010307915
                else:
                    var381 = -1.2135328
            else:
                if input[0] < 4.0:
                    var381 = -0.10055955
                else:
                    var381 = 0.51510155
        else:
            if input[8] < 38.0:
                if input[4] < 203.704:
                    var381 = 0.66819876
                else:
                    var381 = -0.8000623
            else:
                if input[8] < 83.0:
                    var381 = 1.3433726
                else:
                    var381 = 0.0005316162
    else:
        if input[6] < 34.0:
            if input[7] < 29.0:
                if input[7] < 22.0:
                    var381 = -0.4463791
                else:
                    var381 = 0.43437982
            else:
                if input[1] < 1038.0:
                    var381 = -1.3735613
                else:
                    var381 = 0.19740753
        else:
            if input[6] < 41.0:
                if input[1] < 623.0:
                    var381 = 0.026908366
                else:
                    var381 = 1.3110081
            else:
                if input[7] < 34.0:
                    var381 = -0.79164904
                else:
                    var381 = 0.35098064
    if input[3] < 9.375:
        if input[3] < 8.2:
            if input[8] < 71.0:
                if input[1] < 19.0:
                    var382 = -0.72266436
                else:
                    var382 = 0.32904613
            else:
                if input[8] < 91.0:
                    var382 = 1.3724073
                else:
                    var382 = -0.14800905
        else:
            if input[2] < 507.59:
                var382 = 0.23874055
            else:
                var382 = 1.7222973
    else:
        if input[3] < 44.5:
            if input[3] < 43.0:
                if input[1] < 483.0:
                    var382 = -0.21253069
                else:
                    var382 = 1.3107871
            else:
                if input[0] < 4.0:
                    var382 = 0.41550905
                else:
                    var382 = -2.4945776
        else:
            if input[3] < 55.0:
                if input[9] < 5.0:
                    var382 = -0.57843924
                else:
                    var382 = 1.0079072
            else:
                if input[3] < 60.636364:
                    var382 = -0.47459808
                else:
                    var382 = -0.020165635
    if input[8] < 52.0:
        if input[8] < 49.0:
            if input[5] < 23.0:
                if input[0] < 11.0:
                    var383 = 0.088672526
                else:
                    var383 = -0.23371367
            else:
                if input[2] < 999.45:
                    var383 = -1.5824646
                else:
                    var383 = -0.076161414
        else:
            if input[2] < 1059.79:
                if input[2] < 350.58:
                    var383 = 1.5027622
                else:
                    var383 = -0.38039342
            else:
                if input[8] < 50.0:
                    var383 = -4.264194
                else:
                    var383 = 0.24422346
    else:
        if input[4] < 174.75:
            if input[4] < 164.8211:
                if input[3] < 65.77778:
                    var383 = -0.20271043
                else:
                    var383 = 0.24740534
            else:
                if input[8] < 74.0:
                    var383 = -2.0572264
                else:
                    var383 = -0.083459474
        else:
            if input[8] < 81.0:
                if input[4] < 252.57286:
                    var383 = 1.1207601
                else:
                    var383 = 0.16055292
            else:
                if input[4] < 254.578:
                    var383 = -0.7049148
                else:
                    var383 = 0.17790757
    if input[3] < 116.71429:
        if input[1] < 1020.0:
            if input[1] < 965.0:
                if input[3] < 115.75:
                    var384 = 0.081328094
                else:
                    var384 = 1.3663162
            else:
                if input[8] < 63.0:
                    var384 = -0.27276048
                else:
                    var384 = -2.2968242
        else:
            if input[4] < 128.05:
                if input[4] < 66.75667:
                    var384 = 0.107001744
                else:
                    var384 = 1.8607867
            else:
                if input[2] < 2109.93:
                    var384 = -0.6561083
                else:
                    var384 = 0.5237671
    else:
        if input[3] < 126.833336:
            if input[1] < 1109.0:
                if input[4] < 70.6:
                    var384 = -1.5049921
                else:
                    var384 = -0.3288564
            else:
                var384 = -2.3310263
        else:
            if input[3] < 130.2:
                if input[8] < 81.0:
                    var384 = 1.9284878
                else:
                    var384 = -0.66264343
            else:
                if input[0] < 6.0:
                    var384 = -0.031461313
                else:
                    var384 = -0.5337576
    if input[8] < 89.0:
        if input[1] < 560.0:
            if input[1] < 483.0:
                if input[2] < 2265.21:
                    var385 = -0.04130682
                else:
                    var385 = 0.51155627
            else:
                if input[8] < 30.0:
                    var385 = 1.8051142
                else:
                    var385 = 0.13131995
        else:
            if input[3] < 142.5:
                if input[1] < 586.0:
                    var385 = -1.7430413
                else:
                    var385 = -0.31899217
            else:
                if input[3] < 145.75:
                    var385 = 1.8149699
                else:
                    var385 = -0.0023173376
    else:
        if input[8] < 93.0:
            if input[3] < 68.38461:
                if input[8] < 90.0:
                    var385 = -0.85960305
                else:
                    var385 = 0.5153236
            else:
                if input[3] < 131.8:
                    var385 = 3.0659463
                else:
                    var385 = 0.19631566
        else:
            if input[1] < 482.0:
                if input[1] < 222.0:
                    var385 = 0.21777461
                else:
                    var385 = -0.88510436
            else:
                if input[4] < 70.6:
                    var385 = 1.5503849
                else:
                    var385 = 0.005183792
    if input[1] < 893.0:
        if input[4] < 133.09222:
            if input[2] < 808.38:
                if input[1] < 836.0:
                    var386 = 0.0041536493
                else:
                    var386 = 1.2659622
            else:
                if input[3] < 40.166668:
                    var386 = -0.1386925
                else:
                    var386 = -1.3990132
        else:
            if input[2] < 716.7:
                if input[4] < 135.67334:
                    var386 = -2.9114075
                else:
                    var386 = -0.1751505
            else:
                if input[4] < 142.3689:
                    var386 = 1.2367529
                else:
                    var386 = 0.17833997
    else:
        if input[7] < 19.0:
            if input[3] < 145.75:
                if input[2] < 1630.25:
                    var386 = 0.29004335
                else:
                    var386 = -0.41327477
            else:
                if input[3] < 154.0:
                    var386 = -1.9456978
                else:
                    var386 = -0.4971234
        else:
            if input[2] < 1549.86:
                if input[1] < 1145.0:
                    var386 = -0.26097906
                else:
                    var386 = 0.7435303
            else:
                if input[2] < 2013.45:
                    var386 = 1.1725816
                else:
                    var386 = 0.3370097
    if input[8] < 10.0:
        if input[4] < 145.96428:
            if input[2] < 1129.52:
                if input[8] < 6.0:
                    var387 = 0.09094577
                else:
                    var387 = 0.9646897
            else:
                if input[8] < 2.0:
                    var387 = 0.1098999
                else:
                    var387 = 2.9232042
        else:
            if input[8] < 5.0:
                if input[1] < 420.0:
                    var387 = 1.1634156
                else:
                    var387 = -0.19062693
            else:
                if input[0] < 9.0:
                    var387 = -0.9139981
                else:
                    var387 = 0.49855956
    else:
        if input[8] < 12.0:
            if input[1] < 1075.0:
                if input[4] < 219.127:
                    var387 = -1.3633331
                else:
                    var387 = -0.24402466
            else:
                var387 = 0.02512207
        else:
            if input[2] < 39.86:
                if input[1] < 94.0:
                    var387 = -0.14293095
                else:
                    var387 = 0.9492327
            else:
                if input[2] < 47.46:
                    var387 = -2.0534983
                else:
                    var387 = -0.01941422
    if input[8] < 50.0:
        if input[8] < 49.0:
            if input[1] < 1175.0:
                if input[1] < 1139.0:
                    var388 = -0.04335429
                else:
                    var388 = -0.914731
            else:
                if input[9] < 6.0:
                    var388 = 0.22416179
                else:
                    var388 = 1.3286011
        else:
            if input[2] < 407.43:
                if input[1] < 403.0:
                    var388 = 2.1844814
                else:
                    var388 = 0.0345726
            else:
                if input[0] < 5.0:
                    var388 = -1.4191661
                else:
                    var388 = -4.231585
    else:
        if input[8] < 61.0:
            if input[3] < 815.0:
                if input[2] < 517.54:
                    var388 = -0.28630468
                else:
                    var388 = 0.77565604
            else:
                if input[2] < 393.25:
                    var388 = 0.12762605
                else:
                    var388 = -1.2879517
        else:
            if input[1] < 774.0:
                if input[1] < 756.0:
                    var388 = 0.06019341
                else:
                    var388 = 2.3617144
            else:
                if input[1] < 782.17:
                    var388 = -2.1193874
                else:
                    var388 = -0.14764033
    if input[8] < 99.0:
        if input[8] < 98.0:
            if input[8] < 93.0:
                if input[8] < 90.0:
                    var389 = -0.02168802
                else:
                    var389 = 0.4308726
            else:
                if input[4] < 8.236:
                    var389 = 1.2330445
                else:
                    var389 = -0.5144435
        else:
            if input[2] < 1404.28:
                if input[2] < 347.82:
                    var389 = 0.08775126
                else:
                    var389 = 1.5507089
            else:
                if input[0] < 9.0:
                    var389 = -0.23168336
                else:
                    var389 = 0.11171875
    else:
        if input[2] < 477.17:
            if input[3] < 141.0:
                if input[0] < 4.0:
                    var389 = 0.10799255
                else:
                    var389 = 0.43572694
            else:
                var389 = -0.16499685
        else:
            if input[2] < 950.23:
                if input[4] < 51.16143:
                    var389 = -0.47155762
                else:
                    var389 = -1.8859338
            else:
                if input[0] < 9.0:
                    var389 = -0.6406372
                else:
                    var389 = 0.4684967
    if input[3] < 752.0:
        if input[8] < 27.0:
            if input[4] < 216.87273:
                if input[2] < 1246.48:
                    var390 = -0.21880046
                else:
                    var390 = 0.5540779
            else:
                if input[1] < 560.0:
                    var390 = -0.037526958
                else:
                    var390 = -0.77430105
        else:
            if input[3] < 470.5:
                if input[4] < 463.0775:
                    var390 = 0.14555036
                else:
                    var390 = -0.24563776
            else:
                if input[8] < 61.0:
                    var390 = 1.327734
                else:
                    var390 = 0.30983278
    else:
        if input[2] < 1815.6:
            if input[8] < 85.0:
                if input[1] < 1038.0:
                    var390 = -1.8367735
                else:
                    var390 = -0.23283051
            else:
                if input[1] < 816.0:
                    var390 = -0.16793671
                else:
                    var390 = 0.78403115
        else:
            if input[1] < 828.0:
                if input[1] < 793.0:
                    var390 = 0.05817566
                else:
                    var390 = -0.4700399
            else:
                var390 = 0.642489
    if input[3] < 79.916664:
        if input[3] < 79.166664:
            if input[1] < 774.0:
                if input[1] < 697.0:
                    var391 = 0.046296548
                else:
                    var391 = 1.0053293
            else:
                if input[4] < 162.135:
                    var391 = -0.8123315
                else:
                    var391 = 0.9900528
        else:
            if input[8] < 30.0:
                if input[0] < 5.0:
                    var391 = 0.44696656
                else:
                    var391 = 3.6566632
            else:
                if input[0] < 11.0:
                    var391 = -1.7981833
                else:
                    var391 = 0.2980835
    else:
        if input[1] < 916.0:
            if input[1] < 904.0:
                if input[0] < 6.0:
                    var391 = -0.020040466
                else:
                    var391 = -0.5044587
            else:
                if input[4] < 113.816666:
                    var391 = 0.19458415
                else:
                    var391 = -2.0976248
        else:
            if input[1] < 924.0:
                if input[2] < 1049.84:
                    var391 = 3.3754852
                else:
                    var391 = -0.46937463
            else:
                if input[3] < 85.0:
                    var391 = -0.65734595
                else:
                    var391 = 0.15848051
    if input[8] < 4.0:
        if input[2] < 1922.45:
            if input[4] < 145.96428:
                if input[2] < 517.54:
                    var392 = 0.8045031
                else:
                    var392 = -0.51267624
            else:
                if input[4] < 254.578:
                    var392 = 1.4694866
                else:
                    var392 = 0.1367212
        else:
            if input[0] < 6.0:
                var392 = -0.99232787
            else:
                if input[3] < 66.666664:
                    var392 = -0.19055633
                else:
                    var392 = 0.025616456
    else:
        if input[8] < 8.0:
            if input[0] < 12.0:
                if input[4] < 344.00287:
                    var392 = -0.7736671
                else:
                    var392 = 0.18488769
            else:
                if input[2] < 1129.52:
                    var392 = -0.38673338
                else:
                    var392 = 1.5688981
        else:
            if input[8] < 9.0:
                if input[0] < 11.0:
                    var392 = 1.9597813
                else:
                    var392 = -1.3691081
            else:
                if input[8] < 13.0:
                    var392 = -0.5290465
                else:
                    var392 = 0.008290245
    if input[8] < 19.0:
        if input[2] < 852.7:
            if input[0] < 6.0:
                if input[8] < 4.0:
                    var393 = 0.55001795
                else:
                    var393 = -0.47553667
            else:
                if input[4] < 16.933332:
                    var393 = -0.85873336
                else:
                    var393 = 0.8137447
        else:
            if input[4] < 131.048:
                if input[8] < 12.0:
                    var393 = -1.6237262
                else:
                    var393 = -0.41941267
            else:
                if input[4] < 135.67334:
                    var393 = 2.4969575
                else:
                    var393 = -0.19841655
    else:
        if input[9] < 25.0:
            if input[4] < 582.37:
                if input[6] < 49.0:
                    var393 = 0.098707795
                else:
                    var393 = -0.65380484
            else:
                if input[1] < 508.0:
                    var393 = 0.04303589
                else:
                    var393 = 1.4586548
        else:
            if input[7] < 19.0:
                if input[2] < 2440.91:
                    var393 = -0.5729896
                else:
                    var393 = 0.71024376
            else:
                if input[2] < 1690.22:
                    var393 = -0.23800802
                else:
                    var393 = 0.832348
    if input[2] < 1143.58:
        if input[2] < 1072.44:
            if input[4] < 185.128:
                if input[4] < 119.08143:
                    var394 = 0.019972576
                else:
                    var394 = -0.50948495
            else:
                if input[3] < 264.39:
                    var394 = 1.0017029
                else:
                    var394 = -0.22193675
        else:
            if input[0] < 7.0:
                if input[3] < 142.5:
                    var394 = -0.9626973
                else:
                    var394 = -2.3656332
            else:
                if input[3] < 8.2:
                    var394 = -0.7738196
                else:
                    var394 = 0.46919402
    else:
        if input[4] < 86.75:
            var394 = 2.4794047
        else:
            if input[0] < 4.0:
                if input[5] < 11.0:
                    var394 = -0.60859376
                else:
                    var394 = 0.031631637
            else:
                if input[3] < 99.545456:
                    var394 = -0.004296249
                else:
                    var394 = 0.50972193
    if input[0] < 4.0:
        if input[1] < 781.0:
            if input[1] < 718.0:
                if input[2] < 1072.44:
                    var395 = 0.089549266
                else:
                    var395 = -0.4887385
            else:
                if input[2] < 1639.17:
                    var395 = -1.4279685
                else:
                    var395 = -0.03337555
        else:
            if input[1] < 993.0:
                if input[2] < 2166.02:
                    var395 = 0.71530557
                else:
                    var395 = -0.29931816
            else:
                if input[3] < 391.085:
                    var395 = -0.61803764
                else:
                    var395 = 0.31742275
    else:
        if input[0] < 8.0:
            if input[2] < 314.81:
                if input[3] < 21.142857:
                    var395 = -1.3697691
                else:
                    var395 = -0.15249296
            else:
                if input[3] < 45.090908:
                    var395 = -0.14531639
                else:
                    var395 = 0.5247272
        else:
            if input[4] < 71.902:
                if input[4] < 66.75667:
                    var395 = 0.20487964
                else:
                    var395 = 1.9723781
            else:
                if input[3] < 126.0:
                    var395 = -0.07806029
                else:
                    var395 = -1.3618089
    if input[8] < 27.0:
        if input[3] < 89.22222:
            if input[3] < 82.5:
                if input[2] < 1820.8:
                    var396 = -0.10364757
                else:
                    var396 = 0.43091127
            else:
                if input[8] < 9.0:
                    var396 = 0.16857453
                else:
                    var396 = 1.753425
        else:
            if input[3] < 154.0:
                if input[3] < 142.5:
                    var396 = -0.39924738
                else:
                    var396 = -1.7391051
            else:
                if input[0] < 5.0:
                    var396 = -0.29987058
                else:
                    var396 = 1.6200485
    else:
        if input[8] < 49.0:
            if input[1] < 1070.0:
                if input[1] < 976.0:
                    var396 = 0.2305816
                else:
                    var396 = 1.9002646
            else:
                if input[1] < 1153.0:
                    var396 = -0.7706238
                else:
                    var396 = 0.26573002
        else:
            if input[8] < 50.0:
                if input[2] < 568.58:
                    var396 = 1.2880903
                else:
                    var396 = -3.4905972
            else:
                if input[9] < 8.0:
                    var396 = -0.10569173
                else:
                    var396 = 0.24272159
    if input[3] < 82.166664:
        if input[3] < 60.636364:
            if input[3] < 57.642857:
                if input[3] < 44.5:
                    var397 = -0.059427716
                else:
                    var397 = 0.31706214
            else:
                if input[4] < 203.704:
                    var397 = -1.0419123
                else:
                    var397 = 0.7813492
        else:
            if input[3] < 63.1:
                if input[1] < 368.0:
                    var397 = -0.13338509
                else:
                    var397 = 2.003815
            else:
                if input[1] < 697.0:
                    var397 = -0.20126633
                else:
                    var397 = 0.5860634
    else:
        if input[3] < 141.0:
            if input[3] < 139.33333:
                if input[2] < 1742.62:
                    var397 = -0.018072687
                else:
                    var397 = -0.5989692
            else:
                if input[0] < 2.0:
                    var397 = 0.047039416
                else:
                    var397 = -2.3718884
        else:
            if input[7] < 14.0:
                if input[2] < 818.99:
                    var397 = 0.5663852
                else:
                    var397 = 0.058532853
            else:
                if input[0] < 3.0:
                    var397 = -0.09922795
                else:
                    var397 = -0.93052167
    if input[1] < 1020.0:
        if input[1] < 1012.0:
            if input[4] < 206.61363:
                if input[1] < 931.0:
                    var398 = -0.010924301
                else:
                    var398 = -0.6664302
            else:
                if input[4] < 271.90875:
                    var398 = 0.56935996
                else:
                    var398 = 0.009234383
        else:
            var398 = -1.8287529
    else:
        if input[1] < 1038.0:
            if input[4] < 37.923077:
                var398 = -1.8890747
            else:
                if input[4] < 129.5:
                    var398 = 2.9804273
                else:
                    var398 = 0.85347646
        else:
            if input[3] < 82.166664:
                if input[1] < 1062.0:
                    var398 = 0.5911865
                else:
                    var398 = 1.8393494
            else:
                if input[1] < 1100.0:
                    var398 = -0.3562989
                else:
                    var398 = 0.26438412
    if input[3] < 250.0:
        if input[1] < 516.0:
            if input[1] < 482.0:
                if input[2] < 1922.45:
                    var399 = 0.12112099
                else:
                    var399 = -0.25020713
            else:
                if input[2] < 78.33:
                    var399 = -0.41580102
                else:
                    var399 = 1.7949421
        else:
            if input[1] < 616.0:
                if input[9] < 15.0:
                    var399 = -0.6582979
                else:
                    var399 = -3.4533088
            else:
                if input[1] < 633.0:
                    var399 = 0.583264
                else:
                    var399 = -0.16718453
    else:
        if input[3] < 302.1:
            if input[1] < 1116.0:
                if input[9] < 25.0:
                    var399 = 1.2505949
                else:
                    var399 = 0.057550557
            else:
                if input[1] < 1182.0:
                    var399 = -1.276298
                else:
                    var399 = 0.69345707
        else:
            if input[3] < 989.0:
                if input[8] < 30.0:
                    var399 = -0.40087375
                else:
                    var399 = 0.18099332
            else:
                if input[2] < 927.74:
                    var399 = 0.2215149
                else:
                    var399 = 0.8423194
    if input[6] < 14.0:
        if input[2] < 655.24:
            if input[3] < 169.28572:
                if input[3] < 162.5:
                    var400 = -0.18414728
                else:
                    var400 = -1.6573018
            else:
                if input[7] < 14.0:
                    var400 = 0.52842885
                else:
                    var400 = -0.29795358
        else:
            if input[3] < 136.14285:
                if input[1] < 643.0:
                    var400 = -0.70020217
                else:
                    var400 = 1.2251847
            else:
                if input[0] < 3.0:
                    var400 = -0.8319031
                else:
                    var400 = -3.4769332
    else:
        if input[2] < 841.11:
            if input[9] < 5.0:
                if input[8] < 76.0:
                    var400 = 1.5693561
                else:
                    var400 = 0.23052107
            else:
                if input[8] < 82.0:
                    var400 = 0.31868473
                else:
                    var400 = -1.4753121
        else:
            if input[2] < 910.41:
                if input[3] < 82.166664:
                    var400 = 0.17671178
                else:
                    var400 = -1.5414212
            else:
                if input[2] < 927.74:
                    var400 = 1.323101
                else:
                    var400 = -0.026119247
    if input[3] < 57.642857:
        if input[1] < 482.0:
            if input[1] < 447.0:
                if input[2] < 2077.07:
                    var401 = 0.029935986
                else:
                    var401 = 0.44647866
            else:
                if input[2] < 2224.29:
                    var401 = -1.2678107
                else:
                    var401 = 0.29621276
        else:
            if input[2] < 2419.86:
                if input[3] < 51.25:
                    var401 = 1.1652824
                else:
                    var401 = 0.18051122
            else:
                var401 = -1.4141377
    else:
        if input[4] < 111.9975:
            if input[4] < 51.994:
                if input[1] < 1025.03:
                    var401 = -0.48415533
                else:
                    var401 = 0.25702882
            else:
                if input[1] < 1145.0:
                    var401 = 0.4526461
                else:
                    var401 = -0.9167615
        else:
            if input[4] < 121.096664:
                if input[4] < 118.291664:
                    var401 = -0.26791432
                else:
                    var401 = -2.3083386
            else:
                if input[4] < 129.5:
                    var401 = 0.64689916
                else:
                    var401 = -0.1328446
    if input[2] < 1807.71:
        if input[2] < 1690.22:
            if input[2] < 1630.25:
                if input[2] < 1143.58:
                    var402 = -0.08689173
                else:
                    var402 = 0.211502
            else:
                if input[4] < 544.2833:
                    var402 = -1.131029
                else:
                    var402 = -0.08570404
        else:
            if input[4] < 219.815:
                if input[4] < 136.49834:
                    var402 = 1.6638464
                else:
                    var402 = -0.8861505
            else:
                if input[0] < 7.0:
                    var402 = 0.36742935
                else:
                    var402 = 2.3411295
    else:
        if input[6] < 38.0:
            if input[3] < 108.375:
                if input[3] < 99.0:
                    var402 = -0.91470814
                else:
                    var402 = -5.095674
            else:
                if input[3] < 130.2:
                    var402 = 1.0350362
                else:
                    var402 = -0.4488996
        else:
            if input[4] < 149.6:
                if input[2] < 2013.45:
                    var402 = 0.28195497
                else:
                    var402 = 2.0141847
            else:
                if input[1] < 1187.0:
                    var402 = -0.19930854
                else:
                    var402 = 1.2301844
    if input[1] < 697.0:
        if input[1] < 447.0:
            if input[9] < 16.0:
                if input[1] < 414.0:
                    var403 = 0.049923256
                else:
                    var403 = 1.004757
            else:
                if input[6] < 49.0:
                    var403 = -0.4841362
                else:
                    var403 = 0.7160754
        else:
            if input[3] < 115.75:
                if input[4] < 375.698:
                    var403 = -0.40361032
                else:
                    var403 = -4.0471344
            else:
                if input[3] < 131.8:
                    var403 = 1.6926087
                else:
                    var403 = -0.11905886
    else:
        if input[1] < 713.0:
            if input[0] < 7.0:
                var403 = 0.2786911
            else:
                var403 = 2.0190187
        else:
            if input[7] < 4.0:
                if input[4] < 187.2825:
                    var403 = 0.0021221791
                else:
                    var403 = -1.1358229
            else:
                if input[3] < 109.888885:
                    var403 = 1.114097
                else:
                    var403 = 0.118735425
    if input[4] < 5.848889:
        if input[8] < 66.0:
            if input[0] < 2.0:
                var404 = -0.45028076
            else:
                var404 = 0.3822867
        else:
            var404 = 1.8945414
    else:
        if input[8] < 32.0:
            if input[2] < 1820.8:
                if input[2] < 519.94:
                    var404 = 0.008984434
                else:
                    var404 = -0.44835716
            else:
                if input[4] < 182.08:
                    var404 = 1.3550441
                else:
                    var404 = -0.052815508
        else:
            if input[8] < 34.0:
                if input[3] < 95.8:
                    var404 = -0.2988385
                else:
                    var404 = 2.4007995
            else:
                if input[8] < 39.0:
                    var404 = -0.35002694
                else:
                    var404 = 0.0012047557
    if input[4] < 71.902:
        if input[2] < 735.52:
            if input[2] < 696.14:
                if input[4] < 64.46167:
                    var405 = 0.09423383
                else:
                    var405 = 0.95006067
            else:
                var405 = -1.445937
        else:
            if input[0] < 14.0:
                if input[1] < 66.13:
                    var405 = 0.93252105
                else:
                    var405 = 3.0543854
            else:
                if input[1] < 810.0:
                    var405 = 0.5446338
                else:
                    var405 = -1.1003815
    else:
        if input[3] < 2.5:
            if input[8] < 68.0:
                if input[8] < 39.0:
                    var405 = -0.54256594
                else:
                    var405 = -1.4048996
            else:
                var405 = -0.09800822
        else:
            if input[6] < 14.0:
                if input[2] < 672.91:
                    var405 = -0.14615774
                else:
                    var405 = -1.5953095
            else:
                if input[2] < 880.17:
                    var405 = 0.63383883
                else:
                    var405 = 0.0010273699
    if input[4] < 93.88143:
        if input[4] < 66.496155:
            if input[3] < 29.333334:
                if input[3] < 10.0:
                    var406 = 0.34678993
                else:
                    var406 = -0.7881555
            else:
                if input[1] < 893.0:
                    var406 = 0.33215743
                else:
                    var406 = -0.3368402
        else:
            if input[1] < 1109.0:
                if input[1] < 976.0:
                    var406 = -0.6755159
                else:
                    var406 = 0.95307684
            else:
                var406 = -2.7051697
    else:
        if input[4] < 95.216:
            if input[1] < 951.0:
                var406 = 3.1763022
            else:
                var406 = -1.7719635
        else:
            if input[3] < 76.0:
                if input[1] < 182.0:
                    var406 = -0.23670517
                else:
                    var406 = 0.35111102
            else:
                if input[3] < 79.166664:
                    var406 = -0.92205507
                else:
                    var406 = -0.025941033
    return var351 + var352 + var353 + var354 + var355 + var356 + var357 + var358 + var359 + var360 + var361 + var362 + var363 + var364 + var365 + var366 + var367 + var368 + var369 + var370 + var371 + var372 + var373 + var374 + var375 + var376 + var377 + var378 + var379 + var380 + var381 + var382 + var383 + var384 + var385 + var386 + var387 + var388 + var389 + var390 + var391 + var392 + var393 + var394 + var395 + var396 + var397 + var398 + var399 + var400 + var401 + var402 + var403 + var404 + var405 + var406
