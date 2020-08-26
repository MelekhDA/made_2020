# Задача 2

## Пользователи

### Гистограмма признаков

![Hist_item_1](archive/user/hist_features_0_15.png)

![Hist_item_2](archive/user/hist_features_16_31.png)

### Корреляция Пирсона (все пирзнаки - численные)

![Corr_user_1](archive/user/features_corr.png)

## Баннеры

### Гистограммы признаков

![Hist_item_1](archive/item/hist_features_0_15.png)

![Hist_item_2](archive/item/hist_features_16_31.png)

### Диаграмма размаха (boxplot) и гистограмма с большим *bins* (количеством интервалов)

#### Диаграмма размаха (выборочно)

![Boxplot_feature_0_3](archive/item/boxplot_features_0_3.png)

#### Гистограмма(выборочно)

![Hist_item_0_max_bins](archive/item/hist_feature_0_max_bins.png)
![Hist_item_1_max_bins](archive/item/hist_feature_1_max_bins.png)
![Hist_item_2_max_bins](archive/item/hist_feature_2_max_bins.png)
![Hist_item_3_max_bins](archive/item/hist_feature_3_max_bins.png)

### Корреляция Пирсона (все признаки - численные)

![Hist_corr_1](archive/item/features_corr_before.png)

### Итерационный поиск выбросов в признаке с именем 0

![Plot_outlier_feature_0](archive/item/plot_iter_drop_outlier.png)

### Итерационный поиск выбросов с усреднением статистики (по которой производится определение шума) по всем признакам

    Банннеры на удаление: [441, 284, 285, 291, 424, 287, 286, 425, 289, 292]

![Plot_outlier_features](archive/item/plot_iter_drop_outlier_by_all_features.png)

### Корреляция после удаления списка баннеров как выброс

#### Первый взгляд

![Hist_corr_2](archive/item/features_corr_after_drop_1.png)

#### Диаграмма размаха признака с именем 16

    К ранее определённым выбросам добавлены ещё два: [441, 284, 285, 291, 424, 287, 286, 425, 289, 292] + [383, 384]

![Boxplot_processed_feature_16](archive/item/boxplot_processed_feature_16.png)

### Корреляция после пополнения списка баннеров в качестве выброса

![Corr_item_3](archive/item/features_corr_after_drop_2.png)

### Дополнительно (для сравнения) - корреляция после робастной нормализации признаков

![Corr_item_4](archive/item/features_corr_after_norm_features.png)

## Лайки-дизлайки

### Разница между количеством лайков и дизлайков для каждого баннера (по всем пользователям)

![Like_dislike](archive/like/like_dislike_by_all_users.png)

### Количество баннеров

    Количество баннеров с лайками: 203
    Количество баннеров без лайков: 241
