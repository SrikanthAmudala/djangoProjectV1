from __future__ import unicode_literals

from django.db.models import Q
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from account.models import Account
from .forms import CreateBlogPostForm
# Create your views here.
from .models import Task
from .serializers import TaskSerializer


@api_view(["POST"])
def sampleAPI(request):
    try:
        result = {"result": "this is working"}
        return Response(result, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def taskList(request):
    """
    Lists the tasks for the user
    """
    try:
        # if request.user.username == "root":
        #     pass

        title = request.data.get("title", None)
        desc = request.data.get("desc", None)
        stat = request.data.get("status", None)
        taskDueDate = request.data.get("taskDueDate", None)
        sortby = request.data.get("sortby", None)
        qs = Task.objects.filter(userID=request.user)
        if sortby:
            qs = qs.order_by(sortby)

        if title:
            qs = qs.filter(Q(title__exact=title))

        if desc:
            qs = qs.filter(Q(desc__exact=desc))

        if stat:
            qs = qs.filter(Q(status__exact=stat))

        if taskDueDate:
            qs = qs.filter(Q(taskDueDate__exact=taskDueDate))

        serializer = TaskSerializer(qs, many=True)
        if len(serializer.data) != 0:
            for i in range(len(serializer.data)):
                serializer.data[i]['userID'] = request.user.username

        return Response(serializer.data, status=status.HTTP_200_OK)


    except Exception as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def createToDO(request):
    """

    :param request:
    :return: Creates the to do item
    """
    try:
        user = request.user
        if not user.is_authenticated:
            return redirect('must_authenticate')

        if request.data['status'] not in ['TODO', 'In Progress', 'Done']:
            return Response({"result": "status should be among TODO or In Progress or Done, please try again!"},
                            status=status.HTTP_200_OK)

        form = CreateBlogPostForm(request.data)
        print(form.is_valid())
        if form.is_valid():
            obj = form.save(commit=False)
            author = Account.objects.filter(email=user.email).first()
            obj.userID = author
            obj.save()
            return Response(form.data, status=status.HTTP_200_OK)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def taskUpdate(request):
    try:
        title = request.data.get("title", None)
        if not title:
            raise ValueError({"error": "title is empty"})

        task = Task.objects.get(title=title)
        user = request.user
        if task.userID != user:
            return Response({"result": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def taskDelete(request):
    try:
        title = request.data.get("title", None)
        if not id:
            raise ValueError({"error": "title is empty"})

        task = Task.objects.get(title=title)

        user = request.user
        print(task.userID)
        print(user)
        if task.userID != user:
            return Response({"result": "Access Denied"}, status=status.HTTP_401_UNAUTHORIZED)

        task.delete()
        return Response(True, status=status.HTTP_200_OK)

    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
