# 坐标信息总表
-- 商家ID,存疑备注,经度,纬度,地址,存疑人,存疑时间
SELECT
task.wm_poi_id,cunyi.remark,e.longitude,e.latitude,e.address,em.name,FROM_UNIXTIME(cunyi.ctime)

-- 存疑表作为主表
FROM origindb.waimaidata_manage__wm_audit_doubt cunyi
-- 审核任务表，以id相连
-- 同时限定为坐标任务
left join origin_waimai.waimaidata_manage__wm_audit_task task on task.biz_id = cunyi.biz_id and task.biz_type =8 and task.status = 4 and task.valid =1
-- 审核人员表
left join origin_waimai.waimai_cos__dim_wm_employ em on em.uid = cunyi.cuid
-- 商家信息表，用ID链接，不用poi_id，那个门店ID不靠谱
left join origin_waimai.waimai_cos__wm_poi e on e.id = task.wm_poi_id


WHERE
task.biz_type = 8
and task.ctime >= UNIX_TIMESTAMP('2016-12-01 00:00:00')
and task.ctime <= UNIX_TIMESTAMP('2016-12-12 23:59:59')


# 这个坐标存疑更靠谱些，确定了最后一次存疑时间
-- 商家ID,存疑备注,经度,纬度,地址,存疑人,存疑时间
SELECT
DISTINCT
arse.id,adse.remark,e.longitude,e.latitude,e.address,em.name,FROM_UNIXTIME(arse.ctime)

-- 存疑表作为主表
FROM
  (
    SELECT ar.id as id,ar.biz_id as biz_id,max(ad.ctime) as ctime
    FROM
    (
		SELECT b.wm_poi_id as id, max(a.biz_id) as biz_id
		FROM origindb.waimaidata_manage__wm_audit_doubt a
		left join origin_waimai.waimaidata_manage__wm_audit_task b on b.biz_id =a.biz_id and b.biz_type =8 and b.valid =1 and b.status =4
		WHERE a.biz_type =8
  		and a.ctime>=UNIX_TIMESTAMP('2016-10-01 00:00:00')
  		GROUP BY b.wm_poi_id
	) ar
    left join origindb.waimaidata_manage__wm_audit_doubt ad on ad.biz_id = ar.biz_id and ad.biz_type =8
	WHERE ad.ctime>=UNIX_TIMESTAMP('2016-10-01 00:00:00')
    GROUP BY ar.id,ar.biz_id
  ) arse
left join origindb.waimaidata_manage__wm_audit_doubt adse on adse.biz_id = arse.biz_id and adse.ctime= arse.ctime and adse.biz_type =8
left join origin_waimai.waimai_cos__dim_wm_employ em on em.uid = adse.cuid
left join origin_waimai.waimai_cos__wm_poi e on e.id = arse.id


WHERE
adse.ctime>=UNIX_TIMESTAMP('2016-10-01 00:00:00')


-- 商家ID,商家名称,责任BD,蜂窝,蜂窝属性,城市团队,区域,是否代理商,是否电销,最后一次下线操作时间,最后一次下线操作原因,最后一次下线操作人,最后一次上线操作时间,最后一次上线操作原因,最后一次上线操作人
select
uu.upid,c.poi_name,c.bd_name,c.aor_name,if(c.aor_type=0,'未知',if(c.aor_type=1,'校园','白领')),e2.parent_name,
e1.parent_name,max(if(e.source=50,1,0)),dig.ec_label,from_unixtime(uu.utime),uu.uremark,uu.uname,
from_unixtime(uu.dtime),uu.dremark,uu.dname

from
(
	select
	distinct
		zzz.id as upid,zzz.uti as utime,zzz.ur as uremark,zzz.un as uname,zzz.dti as dtime,do2.remark as dremark,do2.op_uname as dname
	from
		(
		select
			zz.id as id,zz.ut as uti ,zz.ur as ur,zz.un as un,max(do.ctime) as dti
		from
			(
				select
				distinct
				z.id as id,z.ti as ut,dp.remark as ur,dp.op_uname as un
				from
				(
					select

						d.wm_poi_id as id,max(d.ctime) as ti
					from
						origin_waimai.waimai_cos__wm_poi_op_log d
					where
						d.dt>=$begincomp
						and d.dt<=$endcomp
						and d.op_type =19
					group by
						d.wm_poi_id
				) z
				left join origin_waimai.waimai_cos__wm_poi_op_log dp on z.id=dp.wm_poi_id and z.ti=dp.ctime and dp.op_type=19
				where
					dp.dt>=$begincomp
					and
					dp.dt<=$endcomp
			) zz
		left join origin_waimai.waimai_cos__wm_poi_op_log do on zz.id=do.wm_poi_id and do.op_type=18

		group by
			zz.id,zz.ut,zz.ur,zz.un
		) zzz
	left join origin_waimai.waimai_cos__wm_poi_op_log do2 on zzz.id=do2.wm_poi_id and zzz.dti=do2.ctime and do2.op_type=18

) uu
left join mart_waimai.dim_poi_level c on c.poi_id=uu.upid
left join origindb.waimaidata_manage__wm_audit_task_batch e on e.wm_poi_id=c.poi_id
left join mart_waimai.dim_wm_org_aor_redundancy e1 on c.aor_id=e1.leaf_value and e1.level=4
left join mart_waimai.dim_wm_org_aor_redundancy e2 on c.aor_id=e2.leaf_value and e2.level=5
left join origin_waimai.waimai_poi__wm_poi_extension dig on dig.wm_poi_id=c.poi_id
GROUP BY
uu.upid,c.poi_name,c.bd_name,c.aor_name,if(c.aor_type=0,'未知',if(c.aor_type=1,'校园','白领')),e2.parent_name,
e1.parent_name,dig.ec_label,from_unixtime(uu.utime),uu.uremark,uu.uname,
from_unixtime(uu.dtime),uu.dremark,uu.dname



-- 商家ID,修改任务ID,新建任务ID,修改任务地址,新建任务地址,当前地址,营业执照地址,物理城市,责任BD,城市团队,提交人,提审时间,审核时间,审核人

select
aa.wm_poi_id,a.batch_id,c.batch_id,json_extract(d.data,'$.address'),json_extract(b.data,'$.address'),g.address,q.address,
g.city_name,g.bd_name,e2.parent_name,em.name,from_unixtime(a.submit_time),from_unixtime(a.utime),emu.name
from
  (
    SELECT
      max(a.id) as id,a.wm_poi_id as wm_poi_id
    FROM
      origin_waimai.waimaidata_manage__wm_audit_task a
    WHERE
      a.biz_type=8
      and a.op_type=2
      and a.status =4
      and a.utime<=UNIX_TIMESTAMP(CONCAT('$yesterday','23:59:59'))
      and a.utime>=UNIX_TIMESTAMP(CONCAT('$yesterday','00:00:00'))
      group by a.wm_poi_id
  ) aa
left JOIN origindb.waimaidata_manage__wm_audit_task_data b on aa.id=b.wm_audit_task_id and b.biz_type=8
left join origin_waimai.waimaidata_manage__wm_audit_task c on c.wm_poi_id=aa.wm_poi_id and c.op_type=1 and c.biz_type=8
left JOIN origindb.waimaidata_manage__wm_audit_task_data d on c.id=d.wm_audit_task_id and d.biz_type=8
left join origin_waimai.waimai_poi__wm_poi_qualification_info q on q.wm_poi_id=aa.wm_poi_id and q.type=1 and q.valid=1
left join mart_waimai.dim_poi_level g on aa.wm_poi_id=g.poi_id
left join mart_waimai.dim_wm_org_aor_redundancy e2 on g.aor_id=e2.leaf_value and e2.level=5
left join origin_waimai.waimaidata_manage__wm_audit_task a on aa.id=a.id and aa.wm_poi_id=a.wm_poi_id and a.op_type=2 and a.biz_type=8
left join origin_waimai.waimai_cos__wm_employ em on a.submit_uid=em.uid
left join origin_waimai.waimai_cos__wm_employ emu on a.muid=emu.uid
