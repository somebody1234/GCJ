javascript:gcjpad=(s,n,c)=>((c||'%20').repeat(Math.ceil(n/(c||'%20').length))+s).slice(-n);gcjtime=n=>{return%20n<1?'--------':`${Math.floor(n/3600)?(gcjpad(Math.floor(n/3600),2)+':'):'%20%20%20'}${gcjpad(Math.floor(n/60)%2560,2,'0')}:${gcjpad(n%2560,2,'0')}`};gcjscore=`%20Place%20%20Rank%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20Name%20%20Points%20%20Penalty%0A`;GCJ.rows.forEach((u,i)=>gcjscore+=`${gcjpad((i+1)+([,'st','nd','rd'][/1?.$/.exec(i+1)]||'th'),6)}%20${gcjpad(u.rank,5)}%20${gcjpad(u.name,20)}%20${gcjpad(u.points,7)}%20${gcjtime(u.penalty)}%0A`);console.log(gcjscore)