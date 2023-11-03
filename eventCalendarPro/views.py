from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render

from calendarApp.models import Event


class DashboardView(LoginRequiredMixin, View):
    login_url = "accounts:signin"
    template_name = "core/dashboard.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # 使用者已登入，執行事件查詢
            events = Event.objects.get_all_events(user=request.user)
            running_events = Event.objects.get_running_events(user=request.user)
            latest_events = Event.objects.filter(user=request.user).order_by("-id")[:10]
            context = {
                "total_event": events.count(),
                "running_events": running_events,
                "latest_events": latest_events,
            }
            return render(request, self.template_name, context)
        else:
            # 使用者未登入，採取適當的處理方式
            # 例如，重新導向到登入頁面或顯示錯誤訊息
            return redirect("accounts:signin")
        

        # '''         

from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
# 可以刪除的
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
# import logging
# # 創建一個名為views的日誌記錄器
@csrf_exempt
@login_required(login_url="signup")
def update_event(request):
    # 添加调试信息
    print("Entered update_event view/進入update_event視圖")

    if request.method == 'POST':
        data = json.loads(request.body)
        # event_id = data.get('eventId')

        # 檢查 eventId 是否為有效的數字
        if not event_id or not event_id.isdigit():
            return JsonResponse({"error": "Invalid eventId/無效的 eventId"}, status=400)

        event_id = int(event_id)  # 將 eventId 轉換為整數

        
        event_id = data['eventId']
        new_start_date = data['newStartDate']
        # print("all", event_id, new_start_date)
        print("Received data: eventId =", event_id, "newStartDate =", new_start_date)

        try:
            event = Event.objects.get(id=event_id)
            event.start_time = new_start_date
            event.save()
            print("A")
            return JsonResponse({"message": "Event updated successfully/活動更新成功"})
        except Event.DoesNotExist:
            print("B")
            return JsonResponse({"error": "Event not found/未找到活動"})
        except Exception as e:
            print("C", e)
            return JsonResponse({"error": "Error updating event/更新事件時出錯: " + str(e)})

    # 如果不是 POST 請求，返回一個適當的 HttpResponse
    return HttpResponse("Invalid request/無效的請求", status=400)


# '''
