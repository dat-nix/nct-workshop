#!/bin/bash
echo ""
echo "╔══════════════════════════════════════╗"
echo "║   NCT CTF Workshop — Starting...     ║"
echo "╚══════════════════════════════════════╝"
echo ""

echo "▶ Khởi động Docker containers..."
docker compose up -d --build

echo ""
echo "▶ Chờ containers sẵn sàng..."
sleep 3

echo "▶ Mở Cloudflare Tunnels..."

# Xóa log cũ trước khi chạy
rm -f /tmp/cf-01.log /tmp/cf-02.log /tmp/cf-03.log /tmp/cf-04.log

# Redirect stderr (nơi cloudflared ghi URL) vào log file
cloudflared tunnel --url http://localhost:5000 2>/tmp/cf-01.log &
CF1_PID=$!
cloudflared tunnel --url http://localhost:5001 2>/tmp/cf-02.log &
CF2_PID=$!
cloudflared tunnel --url http://localhost:5002 2>/tmp/cf-03.log &
CF3_PID=$!
cloudflared tunnel --url http://localhost:5003 2>/tmp/cf-04.log &
CF4_PID=$!

echo "   Đang kết nối... (chờ 15 giây)"
sleep 15

extract_url() {
  grep -o 'https://[a-zA-Z0-9-]*\.trycloudflare\.com' "$1" 2>/dev/null | head -1
}

URL1=$(extract_url /tmp/cf-01.log)
URL2=$(extract_url /tmp/cf-02.log)
URL3=$(extract_url /tmp/cf-03.log)
URL4=$(extract_url /tmp/cf-04.log)

echo ""
echo "╔══════════════════════════════════════════════════════╗"
echo "║              🚀 WORKSHOP READY!                      ║"
echo "╠══════════════════════════════════════════════════════╣"
printf "║  Challenge 01 — Mark The Lyrics\n"
printf "║  %s\n" "${URL1:-(đang kết nối...)}"
echo "║"
printf "║  Challenge 02 — User Profiles (IDOR)\n"
printf "║  %s\n" "${URL2:-(đang kết nối...)}"
echo "║"
printf "║  Challenge 03 — Hidden in robots.txt\n"
printf "║  %s\n" "${URL3:-(đang kết nối...)}"
echo "║"
printf "║  Challenge 04 — What's in the Photo?\n"
printf "║  %s\n" "${URL4:-(đang kết nối...)}"
echo "╚══════════════════════════════════════════════════════╝"
echo ""

if [ -z "$URL1" ] || [ -z "$URL2" ] || [ -z "$URL3" ] || [ -z "$URL4" ]; then
  echo "  ⚠️  Một số tunnel chưa kết nối. Debug:"
  echo "     cat /tmp/cf-01.log"
  echo ""
fi

echo "  Nhấn Ctrl+C để dừng tất cả."
echo ""

trap "echo ''; echo 'Đang dừng...'; kill $CF1_PID $CF2_PID $CF3_PID $CF4_PID 2>/dev/null; docker compose down; echo 'Đã dừng tất cả.'; exit 0" INT

wait
