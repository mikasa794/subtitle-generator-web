import socket
import threading
import sys

# Configuration
LOCAL_PORT = 8888        # Port we listen on (Phone connects here)
UPSTREAM_HOST = '127.0.0.1'
UPSTREAM_PORT = 7897     # SakuraCat Port

def bridge(source, dest, name):
    try:
        while True:
            data = source.recv(16384)
            if not data:
                break
            dest.sendall(data)
    except Exception:
        pass
    finally:
        try:
            source.shutdown(socket.SHUT_RD)
        except:
            pass
        try:
            dest.shutdown(socket.SHUT_WR)
        except:
            pass

def handle_client(client_socket, addr):
    upstream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        upstream_socket.connect((UPSTREAM_HOST, UPSTREAM_PORT))
        
        # Start bidirectional bridging
        t1 = threading.Thread(target=bridge, args=(client_socket, upstream_socket, "client->upstream"))
        t2 = threading.Thread(target=bridge, args=(upstream_socket, client_socket, "upstream->client"))
        t1.daemon = True
        t2.daemon = True
        t1.start()
        t2.start()
        
        t1.join()
        t2.join()
    except Exception as e:
        print(f"   Connection failed: {e}")
    finally:
        client_socket.close()
        upstream_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind(('0.0.0.0', LOCAL_PORT))
    except Exception as e:
        print(f"❌ Failed to bind port {LOCAL_PORT}: {e}")
        return

    server.listen(10)
    print(f"🚀 Proxy Relay running on 0.0.0.0:{LOCAL_PORT} -> {UPSTREAM_HOST}:{UPSTREAM_PORT}")
    print("---------------------------------------------------------")
    print(f"ℹ️  INSTRUCTIONS FOR PHONE:")
    print(f"   Server: 192.168.100.30  (Your PC IP)")
    print(f"   Port:   {LOCAL_PORT}")
    print("---------------------------------------------------------")
    
    while True:
        try:
            client, addr = server.accept()
            print(f"⚡ Connection from {addr[0]}")
            t = threading.Thread(target=handle_client, args=(client, addr))
            t.daemon = True
            t.start()
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error accepting connection: {e}")

if __name__ == '__main__':
    main()
