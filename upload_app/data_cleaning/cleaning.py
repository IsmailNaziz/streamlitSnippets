# Création des nouvelles colonnes de base
df_work['date'] = df_work['date_fin_appel'].dt.date
df_work['heure_minute'] = df_work['date_fin_appel'].dt.strftime('%H:%M')


# Calcul du quart d'heure
def get_quarter_hour(dt):
    minute = dt.minute
    quarter_start = (minute // 15) * 15
    quarter_end = quarter_start + 15
    return f"{dt.hour:02d}:{quarter_start:02d}-{dt.hour:02d}:{quarter_end:02d}"

# Week-end (dimanche = 6 dans Python)
df_work['week_end'] = df_work['date_fin_appel'].dt.weekday == 6

# Jours fériés
df_work['is_holiday'] = df_work['date'].apply(lambda x: x in country_holidays_obj)