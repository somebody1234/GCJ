Uses sysutils;
var
	i, t, n, j, k, m, x: integer;
	a: array [0..9] of boolean;
	s: string;
begin
	read(t);
	for i := 1 to t do
	begin
		read(n);
		if n = 0 then
			writeln('Case #', i, ': INSOMNIA')
		else
		begin
			FillChar(a, SizeOf(a), false);
			m := 0;
			for j := 1 to 10000 do
			begin
				s := IntToStr(n * j);
				for k := 1 to length(s) do
				begin
					x := ord(s[k]) - 48;
					if not a[x] then
					begin
						a[x] := true;
						inc(m);
					end;
				end;
				if m = 10 then
				begin
					writeln('Case #', i, ': ', s);
					break;
				end;
			end;
		end;
	end;
end.
