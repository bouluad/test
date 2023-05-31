current_year=$(date +%Y)
current_week=$(date +%V)

if [ -n "$current_year" ] && [ -n "$current_week" ]; then
  string="Centos7_${current_year}_${current_week}"
else
  string="Centos7_default"
fi

echo "$string"
