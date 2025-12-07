import cv2
import mediapipe as mp
import pyautogui

KEY_GAS = 'right'
KEY_BRAKE = 'left'

class DualHandHillClimbController:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        cv2.namedWindow("Dual Hand Controller - Hill Climb Racing", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Dual Hand Controller - Hill Climb Racing", 960, 720)

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.mp_draw = mp.solutions.drawing_utils

        self.left_prev_open = False
        self.right_prev_open = False

        pyautogui.FAILSAFE = False
        pyautogui.PAUSE = 0
    def is_hand_open(self, hand_landmarks):
        """
        Menentukan apakah tangan 'terbuka' berdasarkan posisi jari.
        Mengembalikan True jika >=4 jari lurus.
        """
        thumb_tip = hand_landmarks.landmark[4].y
        index_tip = hand_landmarks.landmark[8].y
        middle_tip = hand_landmarks.landmark[12].y
        ring_tip = hand_landmarks.landmark[16].y
        pinky_tip = hand_landmarks.landmark[20].y

        thumb_mid = hand_landmarks.landmark[3].y
        index_mid = hand_landmarks.landmark[6].y
        middle_mid = hand_landmarks.landmark[10].y
        ring_mid = hand_landmarks.landmark[14].y
        pinky_mid = hand_landmarks.landmark[18].y

        fingers_extended = [
            thumb_tip < thumb_mid,
            index_tip < index_mid,
            middle_tip < middle_mid,
            ring_tip < ring_mid,
            pinky_tip < pinky_mid
        ]
        return sum(fingers_extended) >= 4

    def detect_hands_state(self, frame):
        """
        Mengembalikan:
        - frame (dengan landmark)
        - left_open  (tangan di kiri layar)
        - right_open (tangan di kanan layar)
        """
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)

        left_open = False
        right_open = False

        if results.multi_hand_landmarks:
            hands_info = []

            # Kumpulkan informasi semua tangan
            for hand_landmarks in results.multi_hand_landmarks:
                cx = hand_landmarks.landmark[0].x  # 0 = wrist
                is_open = self.is_hand_open(hand_landmarks)
                hands_info.append((cx, is_open, hand_landmarks))

            # Urutkan tangan berdasarkan posisi x (0 = paling kiri)
            hands_info.sort(key=lambda x: x[0])

            if len(hands_info) == 1:
                cx, is_open, hand_landmarks = hands_info[0]

                # Kalau cuma satu tangan:
                # jika di kiri layar -> rem, kalau di kanan -> gas
                if cx < 0.5:
                    left_open = is_open
                else:
                    right_open = is_open

                self.mp_draw.draw_landmarks(
                    frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                )

            elif len(hands_info) >= 2:
                # tangan paling kiri = rem
                cx_l, is_open_l, hand_l = hands_info[0]
                # tangan paling kanan = gas
                cx_r, is_open_r, hand_r = hands_info[-1]

                left_open = is_open_l
                right_open = is_open_r

                self.mp_draw.draw_landmarks(
                    frame, hand_l, self.mp_hands.HAND_CONNECTIONS
                )
                self.mp_draw.draw_landmarks(
                    frame, hand_r, self.mp_hands.HAND_CONNECTIONS
                )

        return frame, left_open, right_open

    def update_keys(self, left_open, right_open):
        """
        Mengirim keyDown / keyUp berdasarkan perubahan state.
        Kiri  -> KEY_BRAKE
        Kanan -> KEY_GAS
        """

        # -------- Rem (kiri) --------
        if left_open and not self.left_prev_open:
            pyautogui.keyDown(KEY_BRAKE)
        elif not left_open and self.left_prev_open:
            pyautogui.keyUp(KEY_BRAKE)

        # -------- Gas (kanan) --------
        if right_open and not self.right_prev_open:
            pyautogui.keyDown(KEY_GAS)
        elif not right_open and self.right_prev_open:
            pyautogui.keyUp(KEY_GAS)

        self.left_prev_open = left_open
        self.right_prev_open = right_open

    def run(self):
        print("Jalankan game Hill Climb Racing, fokuskan jendela game,")
        print("lalu jalankan script ini. Tekan 'q' di jendela kamera untuk keluar.\n")

        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Gagal membaca kamera.")
                break

            frame = cv2.flip(frame, 1)

            frame, left_open, right_open = self.detect_hands_state(frame)

            # Update tombol keyboard
            self.update_keys(left_open, right_open)

            # ===== Overlay status =====
            text_left = f"LEFT (Brake: {KEY_BRAKE.upper()}) : {'ON' if left_open else 'OFF'}"
            text_right = f"RIGHT (Gas: {KEY_GAS.upper()}) : {'ON' if right_open else 'OFF'}"

            # warna tetap: kiri merah, kanan biru
            left_color = (0, 0, 255)   # BGR -> merah
            right_color = (255, 0, 0)  # BGR -> biru

            cv2.putText(frame, text_left, (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, left_color, 2)
            cv2.putText(frame, text_right, (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, right_color, 2)

            cv2.imshow("Dual Hand Controller - Hill Climb Racing", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # pastikan tombol dilepas saat keluar
        pyautogui.keyUp(KEY_GAS)
        pyautogui.keyUp(KEY_BRAKE)

        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    controller = DualHandHillClimbController()
    controller.run()
