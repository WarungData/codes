python << EOF
import vim, time

dt = time.strftime('%d-%m-%Y %H:%M:%S')
vim.current.buffer.append(dt)

EOF
