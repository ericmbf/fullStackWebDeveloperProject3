create view get_error as select TO_CHAR(log.time :: DATE, 'Mon dd, yyyy') as date, count(*) as req 
    from log where log.status like '%404%' group by date;
create view get_all as select TO_CHAR(log.time :: DATE, 'Mon dd, yyyy') as date, count(*) as req 
    from log group by date;

select get_all.date, ((get_error.req * 100) / get_all.req) as error
    from get_all, get_error 
    where get_all.date = get_error.date and
    get_error.req > (get_all.req * 0.01);

select path, count(*) as views
from articles, log
where path like CONCAT('%', slug)
group by path
order by views desc;

