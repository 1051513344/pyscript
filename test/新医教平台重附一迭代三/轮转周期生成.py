












if __name__ == "__main__":

#     ids = """426
# 427
# 428
# 429
# 430
# 431
# 432
# 433
# 434
# 435
# 442
# 443
# 444
# 445
# 446
# 447
# 448
# 449
# 450
# 451
# 452
# 453
# 454
# 455
# 456
# 457
# 458
# 459
# 460
# 461
# 462
# 463
# 464
# 465
# 466
# 467
# 468
# 469
# 470
# 471
# 472
# 473
# 474
# 475
# 476
# 477
# 478
# 479
# 480
# 481
# 482
# 483
# 484
# 485
# 486
# 487
# 488
# 489
# 490
# 491
# 680
# 681
# 682
# 683
# 684
# 685
# 686
# 687
# 688
# 689
# 690
# 691
# 692
# 693
# 694
# 695
# 696
# 697
# 698
# 699
# 700
# 701
# 702
# 703
# 704
# 705
# 706
# 707
# 708
# 709
# 710
# 711
# 712
# 713
# 714
# 715
# 716
# 717
# 718
# 719
# 720
# 721
# 722
# 723
# 724
# 725
# 726
# 727
# 728
# 729
# 730
# 731
# 732
# 733
# 734
# 735
# 736
# 737
# 738
# 739"""
#     step = 0.25
#     for id in ids.split("\n"):
#         step = str(step).replace(".0", "")
#         sql = f"UPDATE `ucmed2-base`.`ck_commpara` SET `param_value` = '{step}' WHERE `id` = {id};"
#         print(sql)
#         step = float(step)
#         step = step + 0.25

    step = 0.25
    for i in range(120):
        step = str(step).replace(".0", "")
#         sql = f"""INSERT INTO `ucmed2-base`.`ck_commpara` (`param_code`, `param_name`, `param_value`, `param_1`, `param_2`, `param_3`, `param_4`, `param_5`, `param_6`, `param_7`, `param_8`, `param_9`, `param_10`, `param_11`, `param_12`, `param_13`, `param_14`, `param_15`, `param_16`, `param_17`, `param_18`, `param_19`, `param_20`, `start_time`, `end_time`, `created_at`, `updated_at`, `param_type`)
# SELECT 'turn_cycle', '轮转周期，单位月', '{step}', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1
# FROM dual WHERE NOT EXISTS (
# SELECT `param_code`, `param_name`, `param_value` FROM `ucmed2-base`.`ck_commpara`
# WHERE `param_code` = 'turn_cycle' AND `param_name` = '轮转周期，单位月' AND `param_value` = '{step}'
# );
#         """
        sql = f"""INSERT INTO `ucmed2-base`.`ck_commpara` (`param_code`, `param_name`, `param_value`, `param_1`, `param_2`, `param_3`, `param_4`, `param_5`, `param_6`, `param_7`, `param_8`, `param_9`, `param_10`, `param_11`, `param_12`, `param_13`, `param_14`, `param_15`, `param_16`, `param_17`, `param_18`, `param_19`, `param_20`, `start_time`, `end_time`, `created_at`, `updated_at`, `param_type`) VALUES ('turn_cycle', '轮转周期，单位月', '{step}', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1);"""
        print(sql)
        step = float(step)
        step = step + 0.25


