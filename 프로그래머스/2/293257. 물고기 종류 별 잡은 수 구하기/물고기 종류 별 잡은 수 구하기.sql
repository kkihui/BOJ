select count(f1.fish_type) as fish_count, f2.fish_name
from fish_info f1 
join fish_name_info f2
on f1.fish_type = f2.fish_type
group by f2.fish_name
order by fish_count desc;
