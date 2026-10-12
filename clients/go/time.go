package intraoapi42

import (
	"encoding/json"
	"fmt"
	"strings"
	"time"
)

// IntraTime accepts Intra date strings that may be date-only or RFC3339 date-times.
type IntraTime time.Time

// Time exposes the underlying time.Time value.
func (t IntraTime) Time() time.Time {
	return time.Time(t)
}

// MarshalJSON renders the time in RFC3339Nano.
func (t IntraTime) MarshalJSON() ([]byte, error) {
	return json.Marshal(time.Time(t).Format(time.RFC3339Nano))
}

// UnmarshalJSON normalizes common Intra formats before parsing.
func (t *IntraTime) UnmarshalJSON(data []byte) error {
	var raw string
	if err := json.Unmarshal(data, &raw); err != nil {
		return err
	}

	raw = strings.TrimSpace(raw)
	if raw == "" {
		return nil
	}

	parsed, err := parseIntraTime(raw)
	if err != nil {
		return err
	}

	*t = IntraTime(parsed)
	return nil
}

func parseIntraTime(value string) (time.Time, error) {
	layouts := []string{
		time.RFC3339Nano,
		"2006-01-02",
		"2006-01-02T15:04:05",
		"2006-01-02T15:04:05Z07:00",
		"2006-01-02 15:04:05 -07:00",
		"2006-01-02 15:04:05.000 -07:00",
		"2006-01-02 15:04:05.000000 -07:00",
	}

	for _, layout := range layouts {
		if ts, err := time.Parse(layout, value); err == nil {
			return ts, nil
		}
	}

	return time.Time{}, fmt.Errorf("unsupported Intra time %q", value)
}
