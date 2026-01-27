// KVStoreLevel1Test.java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.*;

public class KVStoreLevel1Test {

    @Test
    void set_then_get_basic() {
        KVStore s = new KVStore();
        s.Set("A", "B", "E");
        assertEquals("E", s.Get("A", "B"));
    }

    @Test
    void set_overwrite_same_field() {
        KVStore s = new KVStore();
        s.Set("A", "city", "NYC");
        s.Set("A", "city", "SEA");        // overwrite
        assertEquals("SEA", s.Get("A", "city"));
    }

    @Test
    void get_missing_field_returns_empty_string() {
        KVStore s = new KVStore();
        s.Set("A", "B", "E");
        assertEquals("", s.Get("A", "NOPE"));
    }

    @Test
    void get_missing_key_returns_empty_string() {
        KVStore s = new KVStore();
        assertEquals("", s.Get("NO_KEY", "any"));
    }

    @Test
    void delete_existing_field_returns_true_and_removes() {
        KVStore s = new KVStore();
        s.Set("A", "B", "E");
        assertTrue(s.Delete("A", "B"));
        assertEquals("", s.Get("A", "B"));
    }

    @Test
    void delete_missing_field_returns_false() {
        KVStore s = new KVStore();
        s.Set("A", "B", "E");
        assertFalse(s.Delete("A", "NOPE"));
    }

    @Test
    void delete_missing_key_returns_false() {
        KVStore s = new KVStore();
        assertFalse(s.Delete("NO_KEY", "anything"));
    }

    @Test
    void multiple_keys_isolated() {
        KVStore s = new KVStore();
        s.Set("K1", "f", "v1");
        s.Set("K2", "f", "v2");
        assertEquals("v1", s.Get("K1", "f"));
        assertEquals("v2", s.Get("K2", "f"));
        assertEquals("", s.Get("K1", "nope"));
        assertTrue(s.Delete("K2", "f"));
        assertEquals("", s.Get("K2", "f"));
        assertEquals("v1", s.Get("K1", "f")); // unaffected
    }

    @Test
    void case_sensitivity_check() {
        KVStore s = new KVStore();
        s.Set("user", "Name", "A");
        s.Set("User", "name", "B");
        assertEquals("A", s.Get("user", "Name"));
        assertEquals("B", s.Get("User", "name"));
        assertEquals("", s.Get("user", "name")); // different case => missing
    }

    @Test
    void set_value_can_be_empty_string() {
        KVStore s = new KVStore();
        s.Set("A", "blank", "");
        assertEquals("", s.Get("A", "blank")); // still a present field with empty value
        assertTrue(s.Delete("A", "blank"));
        assertEquals("", s.Get("A", "blank"));
    }

    @Test
    void many_fields_under_one_key() {
        KVStore s = new KVStore();
        for (int i = 0; i < 100; i++) {
            s.Set("K", "f" + i, "v" + i);
        }
        assertEquals("v0", s.Get("K", "f0"));
        assertEquals("v99", s.Get("K", "f99"));
        assertTrue(s.Delete("K", "f50"));
        assertEquals("", s.Get("K", "f50"));
    }
}