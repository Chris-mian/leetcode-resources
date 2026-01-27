// KVStore.java
// NOTE: Fill in TODOs. Do NOT change method signatures.

import java.util.*;

public class KVStore {
    // TODO: live state (Level 1/2)
    private Map<String, Map<String, String>> live = new HashMap<>();
    private String EMPTY_STRING = "";
    // TODO: timeline events (Level 3)
    // private static class Event { int ts; Kind kind; String value; Integer ttl; }
    // enum Kind { SET, SET_TTL, DEL }
    // private Map<String, Map<String, List<Event>>> timeline = new HashMap<>();

    // ---------- Level 1 ----------
    public void Set(String key, String field, String value) {
        // TODO
        if (live.containsKey(key)) {
            Map<String, String> keyMap = this.live.get(key);
            keyMap.put(field, value);
        } else {
            Map<String, String> keyMap = new HashMap();
            keyMap.put(field,value);
            live.put(key, keyMap);
        }
    }

    public String Get(String key, String field) {
        if (live.containsKey(key)) {
            Map<String, String> keyMap = this.live.get(key);
            return keyMap.getOrDefault(field, EMPTY_STRING);
        } else {
            return EMPTY_STRING;
        }
    }

    public boolean Delete(String key, String field) {
        if (live.containsKey(key)) {
            Map<String, String> keyMap = this.live.get(key);
            if (keyMap.remove(field) != null) {
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
    }

    // ---------- Level 2 ----------
    public String Scan(String key) {
        // return ["f1(v1)", ...] sorted lexicographically by field
        // TODO
        if (live.containsKey(key)) {
            return live.get(key).entrySet().stream()
            .map(e -> e.getKey() + "(" + e.getValue() + ")")
            .sorted()
            .toString();
        } else {
            return "";
        }
    }

    public String ScanByPrefix(String key, String prefix) {
        // TODO
        return Collections.emptyList();
    }

    // ---------- Level 3 ----------
    public void SetAt(String key, String field, String value, int timestamp) {
        // TODO
    }

    public void SetAtWithTtl(String key, String field, String value, int timestamp, int ttl) {
        // TODO
    }

    public boolean DeleteAt(String key, String field, int timestamp) {
        // TODO
        return false;
    }

    public String GetAt(String key, String field, int timestamp) {
        // TODO
        return null;
    }

    public List<String> ScanAt(String key, int timestamp) {
        // TODO
        return Collections.emptyList();
    }

    public List<String> ScanByPrefixAt(String key, String prefix, int timestamp) {
        // TODO
        return Collections.emptyList();
    }

    // -------- Optional: minimal CLI for local testing --------
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        KVStore s = new KVStore();
        while (in.hasNextLine()) {
            String[] p = in.nextLine().trim().split("\\s+");
            if (p.length == 0 || p[0].isEmpty()) continue;
            String op = p[0].toUpperCase();
            switch (op) {
                case "SET": {
                    s.Set(p[1], p[2], p[3]);
                    break;
                }
                case "GET": {
                    String res = s.Get(p[1], p[2]);
                    System.out.println(res != null ? res : "nil");
                    break;
                }
                case "DEL": {
                    System.out.println(s.Delete(p[1], p[2]) ? "true" : "false");
                    break;
                }
                case "SCAN": {
                    System.out.println(String.join(",", s.Scan(p[1])));
                    break;
                }
                case "SCANP": {
                    System.out.println(String.join(",", s.ScanByPrefix(p[1], p[2])));
                    break;
                }
                case "SETAT": {
                    s.SetAt(p[1], p[2], p[3], Integer.parseInt(p[4]));
                    break;
                }
                case "SETATTTL": {
                    s.SetAtWithTtl(p[1], p[2], p[3], Integer.parseInt(p[4]), Integer.parseInt(p[5]));
                    break;
                }
                case "DELAT": {
                    System.out.println(s.DeleteAt(p[1], p[2], Integer.parseInt(p[3])) ? "true" : "false");
                    break;
                }
                case "GETAT": {
                    String res = s.GetAt(p[1], p[2], Integer.parseInt(p[3]));
                    System.out.println(res != null ? res : "nil");
                    break;
                }
                case "SCANAT": {
                    System.out.println(String.join(",", s.ScanAt(p[1], Integer.parseInt(p[2]))));
                    break;
                }
                case "SCANPAT": {
                    System.out.println(String.join(",", s.ScanByPrefixAt(p[1], p[2], Integer.parseInt(p[3]))));
                    break;
                }
            }
        }
    }
}